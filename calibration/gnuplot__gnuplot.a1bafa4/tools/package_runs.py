import gzip, json, re, shutil, subprocess, tarfile
from pathlib import Path
SUB = Path("/root/.claude/projects/-home-claude/099ee5d6-e52a-56a7-bbd7-e94196564feb/subagents")
CAL = Path("/home/claude/pbtask/ProgramBench/calibration/gnuplot__gnuplot.a1bafa4")
IID = "gnuplot__gnuplot.a1bafa4"
RUNS = {1: "afce83424a6f514d9", 2: "a43efee7ecd1b1245", 3: "a0c33cbd02a6c6e4a", 4: "a9eb5927ae7d77b88",
        5: "a26ed6ff1a86e47f3", 6: "a3ecb89adbfe6729a", 7: "a9955ddb7be0628b7", 8: "a8173af85dcbf3fc2"}
ABORTED = {5: "a9e266d7174c01d62", 6: "a1598bbb891fe43a0", 7: "ad1f6c2798a5ccadb", 8: "a4f65428ad0c2163c"}
SUSPICIOUS = [r"/home/claude", r"/root/", r"/tmp/cal/run_0(?!{n})\d", r"\bstrings\s", r"objdump", r"\bcurl\b",
              r"pip3? install", r"go get", r"\bwget\b", r"find /\s", r"WebFetch|WebSearch"]

def stats(path, n):
    ts, models, versions, tools, usage = [], set(), set(), 0, {"input_tokens": 0, "output_tokens": 0,
                                                              "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}
    flags = {}
    for line in open(path):
        d = json.loads(line)
        if d.get("timestamp"): ts.append(d["timestamp"])
        if d.get("version"): versions.add(d["version"])
        m = d.get("message") or {}
        if m.get("model"): models.add(m["model"])
        for k in usage:
            usage[k] += int((m.get("usage") or {}).get(k) or 0)
        for c in m.get("content") or [] if isinstance(m.get("content"), list) else []:
            if c.get("type") == "tool_use":
                tools += 1
                if c.get("name") != "Bash":
                    continue
                cmd = json.dumps(c.get("input"))
                for pat in SUSPICIOUS:
                    p = pat.replace("{n}", str(n))
                    if re.search(p, cmd):
                        flags.setdefault(p, []).append(cmd[:160])
    return {"start": min(ts), "end": max(ts), "models": sorted(models), "agent_versions": sorted(versions),
            "tool_calls": tools, "usage": usage, "audit_flags": {k: v[:5] for k, v in flags.items()}}

out = {}
for n, aid in RUNS.items():
    rd = CAL / "runs" / f"run_{n:02d}"
    shutil.rmtree(rd, ignore_errors=True)
    (rd / IID).mkdir(parents=True)
    src = SUB / f"agent-{aid}.jsonl"
    with open(src, "rb") as f, gzip.open(rd / "trajectory.jsonl.gz", "wb", compresslevel=9) as g:
        shutil.copyfileobj(f, g)
    sol = Path(f"/tmp/cal/run_{n:02d}/ws/solution")
    with tarfile.open(rd / IID / "submission.tar.gz", "w:gz") as t:
        for p in sorted(sol.iterdir()):
            if p.name not in ("executable", ".gocache", ".cache", "gocache", ".gopath"):
                t.add(p, arcname=p.name)
    meta = {"run": f"run_{n:02d}", "agent_id": aid, "frozen_revision": "b62a6b5b47e08edc2d67460a9498457d44a83f7b",
            "agent": "Claude general-purpose sub-agent (Claude Code SDK), tools: Bash, Read, Write, Edit, Glob, Grep",
            "prompt": "calibration/gnuplot__gnuplot.a1bafa4/PROMPT.md with {WS}=" + f"/tmp/cal/run_{n:02d}/ws",
            "budget": {"wall_clock": "instructed ~90 min, single session", "token_cap": None, "turn_cap": None},
            **stats(src, n)}
    (rd / "meta.json").write_text(json.dumps(meta, indent=1))
    out[n] = meta
ab = CAL / "runs" / "_aborted_rate_limited"
ab.mkdir(parents=True, exist_ok=True)
for n, aid in ABORTED.items():
    src = SUB / f"agent-{aid}.jsonl"
    with open(src, "rb") as f, gzip.open(ab / f"run_{n:02d}_attempt1.trajectory.jsonl.gz", "wb", compresslevel=9) as g:
        shutil.copyfileobj(f, g)
    s = stats(src, n)
    out[f"aborted_{n}"] = {"start": s["start"], "end": s["end"], "tool_calls": s["tool_calls"]}
print(json.dumps({k: {kk: v[kk] for kk in ("start", "end", "tool_calls") } | ({"models": v["models"], "flags": list(v["audit_flags"]), "usage": v["usage"]} if "models" in v else {}) for k, v in out.items()}, indent=1))
