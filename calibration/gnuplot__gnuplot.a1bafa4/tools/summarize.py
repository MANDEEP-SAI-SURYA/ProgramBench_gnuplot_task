#!/usr/bin/env python3
"""Recompute summary.json from runs/run_*/ (eval.json written by `programbench eval`, meta.json)."""
import json
import statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
IID = "gnuplot__gnuplot.a1bafa4"
rows, mods = [], defaultdict(list)
for rd in sorted((HERE / "runs").glob("run_*")):
    ev = json.loads((rd / IID / f"{IID}.eval.json").read_text())
    meta = json.loads((rd / "meta.json").read_text())
    tr = ev["test_results"]
    passed = sum(t["status"] == "passed" for t in tr)
    per = defaultdict(lambda: [0, 0])
    for t in tr:
        m = t["name"].split(".")[2]
        per[m][1] += 1
        per[m][0] += t["status"] == "passed"
    for m, (a, b) in per.items():
        mods[m].append(a / b)
    t0, t1 = (datetime.fromisoformat(meta[k].rstrip("Z")) for k in ("start", "end"))
    u = meta["usage"]
    rows.append({"run": rd.name, "passed": passed, "total": len(tr), "score_pct": round(100 * passed / len(tr), 2),
                 "wall_min": round((t1 - t0).total_seconds() / 60, 1), "tool_calls": meta["tool_calls"],
                 "output_tokens": u["output_tokens"],
                 "input_tokens_incl_cache": u["input_tokens"] + u["cache_read_input_tokens"] + u["cache_creation_input_tokens"],
                 "solution_loc": ev["structure"]["nonblank_loc"], "language": ",".join(ev["structure"]["languages"]),
                 "executable_hash": ev["executable_hash"], "verifier": ev["verifier"], "error_code": ev["error_code"]})
sc = [r["score_pct"] for r in rows]
summary = {"instance_id": IID, "frozen_revision": json.loads((HERE / "runs" / "run_01" / "meta.json").read_text())["frozen_revision"],
           "model": "claude-opus-5-5", "runs": rows, "mean_score_pct": round(statistics.mean(sc), 2),
           "stdev_pct": round(statistics.stdev(sc), 2), "min_pct": min(sc), "max_pct": max(sc), "target": "mean < 70%",
           "per_module_mean_pct": {m: round(100 * statistics.mean(v), 1) for m, v in sorted(mods.items())}}
(HERE / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")
print(json.dumps({k: summary[k] for k in ("mean_score_pct", "stdev_pct", "min_pct", "max_pct")}))
