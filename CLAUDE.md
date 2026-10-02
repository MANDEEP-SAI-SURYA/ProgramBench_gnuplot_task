# CLAUDE.md

## Project overview

ProgramBench evaluates whether LM-based SWE agents can reverse-engineer black-box software.
This repository contributes one instance, `gnuplot__gnuplot.a1bafa4`: gnuplot 5.4.9 compiled
into a cleanroom image with the source removed; an agent re-implements it from the binary and
the manual; behavioural tests score the re-implementation.

Do not show anything from `sources/`, `test_authoring/`, `blobs/` or `src/programbench/data/`
to a solving agent. The only agent-visible material is `images/<iid>/task_cleanroom/workspace/`.

## Test ignore reasons

Same vocabulary as upstream (`branches.<hash>.ignored_tests[].reasons[].id` in tests.json):
`gold_fail`, `gold_flaky`, `dummy_pass`, `outcome_dependent_presence`, `slow_or_hang`,
`dependency_ignored`, `ignored_manual`. For this instance problems are removed at authoring
time instead (non-deterministic cases, dummy-passable cases, date-stamped outputs such as
`fit.log` headers and EPS `%%CreationDate`, cases where gnuplot crashes), so every
`ignored_tests` list is empty.

## Quick reference

```bash
python -m pytest tests                                   # harness self-tests
cd src && python -m programbench gold                    # reference + gold submission = 100%
cd src && python -m programbench eval ../runs/<run>      # score submissions
```

## Regenerating tests

See `test_authoring/gnuplot__gnuplot.a1bafa4/README.md`. Golden outputs are produced only by
running the reference binary; never edit them by hand.

## Style

Python ≥ 3.10, standard library only in `src/`, `pathlib` over `os.path`, minimal code,
do not catch exceptions just to re-raise them.
