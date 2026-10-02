"""Submission checks that go beyond upstream's hash-based removal.

* files whose sha256 is in task.yaml `eval_clean_hashes` (the reference binary) are deleted
  before compiling (same as upstream `_remove_hashed_files`);
* an `executable` identical to the reference is rejected;
* any absolute path mentioned in a text file of the workspace that resolves to a copy of the
  reference binary is rejected (catches `exec /somewhere/gnuplot "$@"` wrappers);
* a structure report (languages, LOC) is attached to eval.json for reviewers.
"""
import hashlib
import os
import re
from pathlib import Path

SOURCE_EXT = {
    ".c": "C", ".h": "C", ".cc": "C++", ".cpp": "C++", ".hpp": "C++", ".rs": "Rust", ".go": "Go", ".py": "Python",
    ".js": "JavaScript", ".ts": "TypeScript", ".java": "Java", ".zig": "Zig", ".ml": "OCaml", ".hs": "Haskell",
    ".rb": "Ruby", ".cs": "C#", ".swift": "Swift", ".lua": "Lua", ".sh": "Shell", ".kt": "Kotlin", ".nim": "Nim",
}
SKIP_DIRS = {".git", "target", "node_modules", "__pycache__", "build", "dist", ".cache", "vendor", "eval"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def remove_hashed_files(ws: Path, hashes: set[str]) -> list[str]:
    removed = []
    for p in ws.rglob("*"):
        if p.is_file() and not p.is_symlink() and p.stat().st_size > 100_000 and sha256(p) in hashes:
            removed.append(str(p.relative_to(ws)))
            p.unlink()
    return removed


def references_to_reference(ws: Path, hashes: set[str]) -> list[str]:
    found = []
    for p in ws.rglob("*"):
        if not p.is_file() or p.stat().st_size > 4_000_000 or any(s in SKIP_DIRS for s in p.relative_to(ws).parts):
            continue
        data = p.read_bytes()
        if b"\0" in data[:4096]:
            continue
        for m in set(re.findall(rb"(?:~|/)[^\s\"'`;|&()<>$]+", data)):
            cand = Path(os.path.expanduser(m.decode(errors="ignore")))
            try:
                if cand.is_file() and cand.stat().st_size > 100_000 and sha256(cand) in hashes:
                    found.append(f"{p.relative_to(ws)} -> {cand}")
            except OSError:
                pass
    return found


def structure_report(ws: Path) -> dict:
    langs: dict[str, dict] = {}
    files = 0
    largest = []
    for p in ws.rglob("*"):
        if not p.is_file() or any(s in SKIP_DIRS for s in p.relative_to(ws).parts):
            continue
        files += 1
        lang = SOURCE_EXT.get(p.suffix.lower())
        if not lang:
            continue
        lines = p.read_text(errors="replace").splitlines()
        code = sum(1 for line in lines if line.strip())
        e = langs.setdefault(lang, {"files": 0, "nonblank_loc": 0})
        e["files"] += 1
        e["nonblank_loc"] += code
        largest.append([code, str(p.relative_to(ws))])
    largest.sort(reverse=True)
    return {"files": files, "languages": langs, "nonblank_loc": sum(e["nonblank_loc"] for e in langs.values()),
            "largest_files": largest[:8]}
