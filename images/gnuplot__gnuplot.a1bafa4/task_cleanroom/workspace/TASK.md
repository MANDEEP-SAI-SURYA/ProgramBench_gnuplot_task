# Task: rebuild `gnuplot` from scratch

You are given a compiled program, `./gnuplot` (gnuplot 5.4 patchlevel 9,
Linux x86-64, statically linked, built without X11/Qt/wx/cairo/libgd/lua), and
its user documentation:

* `docs/gnuplot.gih` — the complete gnuplot reference manual (the text that the
  interactive `help` command shows; `GNUHELP=docs/gnuplot.gih ./gnuplot` makes
  `help` work)
* `docs/gnuplot.1` — the man page
* `examples/` — a few scripts with their captured stdout, stderr and exit code

The program's source code is **not** available and you have no internet access.

Your job is to write a **complete, from-scratch implementation** of this
program that behaves identically to `./gnuplot` when run non-interactively.

## What to deliver

A codebase in this directory (any language, any structure) with an executable
script `compile.sh` at its root. Running `./compile.sh` from the root of your
codebase must produce an executable file named `./executable` (in the same
directory) that is a drop-in replacement for `./gnuplot`.

## Rules

* No internet access. `compile.sh` also runs **without network**: it must not
  download anything; use only toolchains and libraries already installed.
* You may run `./gnuplot` as often as you like to observe its behaviour.
* Your `executable` must not invoke, copy, embed or wrap `./gnuplot` or any
  other gnuplot installation. Submissions that do are rejected.
* Do not try to obtain or reconstruct the original source code (no
  decompiling/disassembling, no locally cached copies of gnuplot sources).

## How you will be evaluated

A hidden suite of behavioural tests runs `./executable` in a fresh temporary
directory (environment: `LC_ALL=C.UTF-8`, `HOME` set to that directory) with
command-line options, script files, `-e` commands and standard input, and
compares with the reference:

* standard output, byte for byte;
* standard error, byte for byte (note that `print` writes to stderr by default);
* the exit status;
* for some tests, the contents of files the script writes (`set print`,
  `set output`, `update`, ...).

A test passes only if everything matches. Your score is the percentage of tests
passed. Tests cover: command-line options; the expression language (integers,
floats, complex numbers, strings, arrays, datablocks, user functions, special
functions); `print`, `sprintf` and `gprintf` formatting; control flow
(`do for`, `while`, `if`, `load`, `call`, `eval`, macros); error messages and
their caret lines; `show` output for many settings; `set table` output for
functions and data (`using`, `every`, `index`, missing data, time data, column
headers, `smooth` and `bins` algorithms); `stats` reports; `fit` (iteration log,
final report, variables); plots rendered by the `dumb` terminal (2D and 3D,
all common styles, keys, tics, labels, log scales, multiplot); and a few other
text-based terminals (`svg`, `canvas`).

Where the documentation is silent or imprecise, the behaviour of `./gnuplot`
is the specification.
