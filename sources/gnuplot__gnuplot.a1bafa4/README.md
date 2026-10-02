# Upstream source — gnuplot 5.4.9

Corresponds to the upstream repository checked out at the pinned commit (upstream ProgramBench
keeps it inside the `:task_v6` image only).

* `upstream/` — unmodified `git archive` of tag `5.4.9` (commit `a1bafa410d3c07d832f81884c5af61dee73fb1c5`).
* `patches/0001-post.trm-fix-build-without-deflate-encoder.patch` — build-only fix (unbalanced
  brace in the PostScript driver when no PNG/deflate encoder is configured). No behaviour change.
* `build.sh` — offline, reproducible build → `bin/gnuplot` (static, stripped, `--build-id=none`)
  and `bin/gnuplot.gih` (manual). Needs gcc, make, autoconf, automake, bison, zlib headers.

After rebuilding, update `images/<iid>/task_cleanroom/workspace/gnuplot`, `.../docs/gnuplot.gih`
and `eval_clean_hashes` in `src/programbench/data/tasks/<iid>/task.yaml`.
