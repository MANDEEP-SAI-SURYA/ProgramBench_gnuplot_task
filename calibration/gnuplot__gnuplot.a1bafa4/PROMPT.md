You are an AI coding agent being evaluated on a "rebuild the program from its binary" benchmark task (ProgramBench style).

Your ENTIRE world is the directory {WS}. It contains:
- ./gnuplot : a compiled Linux x86-64 executable (the reference program, gnuplot 5.4.9)
- ./docs/ : its documentation (full reference manual gnuplot.gih, man page)
- ./TASK.md : the task statement (read it first and follow it exactly)
- ./examples/ : a few scripts with captured outputs

STRICT RULES (this is a benchmark; violating them invalidates the run):
1. Do NOT read, list, search or access any file or directory outside {WS} (no `find /`, no looking in /home, /root, other /tmp dirs, system source trees, package caches, etc.). Do not look for hidden tests or source code.
2. Do NOT use the internet (no web search/fetch, no package downloads of any kind). Use only the Go, C or Python standard libraries / toolchains already installed.
3. Do NOT decompile, disassemble or run `strings`/`objdump` on ./gnuplot; learn its behaviour only by running it and reading the docs. Do not reproduce upstream gnuplot source code from memory — design your own implementation.
4. Your implementation must not call, copy, embed or wrap ./gnuplot or any other gnuplot.
5. Always run the reference as `LC_ALL=C.UTF-8 ./gnuplot ...` (the hidden tests use that locale).

Your job: write a from-scratch implementation in {WS}/solution/ with a `compile.sh` at {WS}/solution/compile.sh that, when run from inside {WS}/solution, produces {WS}/solution/executable — a drop-in replacement for ./gnuplot for non-interactive use. If you use Go, use only the standard library and set GOFLAGS=-mod=mod GOPROXY=off GOTOOLCHAIN=local in compile.sh. Hidden tests compare stdout, stderr and exit status byte-for-byte (see TASK.md for the covered areas: CLI, expressions, print/sprintf/gprintf, control flow, error messages with carets, show output, set table output incl. smoothing, stats, fit, dumb-terminal plots, svg/canvas).

Work as you would in a real benchmark run: probe the reference extensively, compare your executable against it on many inputs (differential testing encouraged), prioritise by breadth, and iterate. You have a limited budget: aim to wrap up within roughly 90 minutes of work. Before finishing make sure compile.sh works from a clean state, then reply with a short summary: language, approximate LOC, and the areas you think are weakest.
