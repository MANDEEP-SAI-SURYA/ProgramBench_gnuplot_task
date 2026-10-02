# Contributing

* Harness code lives in `src/programbench/`; keep it standard-library only.
* Never edit golden outputs by hand. Change `test_authoring/<instance_id>/cases_src.py`, then
  regenerate (see `test_authoring/<instance_id>/README.md`) and run `python -m pytest tests`.
* Any change to the reference build (`sources/<instance_id>/`) must update `eval_clean_hashes`
  in `src/programbench/data/tasks/<instance_id>/task.yaml` and the binary under
  `images/<instance_id>/task_cleanroom/workspace/`.
* Before sending a task for review: `python -m programbench gold` must report 100% for both
  the reference binary and the gold submission.
