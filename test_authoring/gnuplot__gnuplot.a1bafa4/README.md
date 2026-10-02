# Test authoring — gnuplot__gnuplot.a1bafa4

Corresponds to the upstream step where tests are written and stored as per-branch archives.

| File | Role |
|---|---|
| `cases_src.py` | every test case (argv, script files, stdin, files to check), grouped by category; includes the difficulty-tuning round |
| `gen_goldens.py` | runs the reference twice per case, stores stdout/stderr/exit/files as golden JSON, rejects non-deterministic cases and drops dummy-passable ones |
| `build_branches.py` | turns goldens into pytest test branches (`branches/<id>/eval/...`), packs `blobs/<iid>/tests/<id>.tar.gz` and writes `tests.json` |
| `branches/<id>/` | readable copy of each test branch (identical to the tarball contents) |

Regenerate everything:

```bash
cd sources/gnuplot__gnuplot.a1bafa4 && ./build.sh && cd -
python3 test_authoring/gnuplot__gnuplot.a1bafa4/gen_goldens.py \
    sources/gnuplot__gnuplot.a1bafa4/bin/gnuplot /tmp/goldens
python3 test_authoring/gnuplot__gnuplot.a1bafa4/build_branches.py /tmp/goldens .
python3 -m pytest tests
```
