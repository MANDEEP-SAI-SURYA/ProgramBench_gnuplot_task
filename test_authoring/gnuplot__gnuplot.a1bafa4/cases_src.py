"""Hidden-test case definitions for the gnuplot 5.4.9 task.

Every case runs the executable once in a fresh temporary directory with
LC_ALL=C.UTF-8 and HOME set to that directory. Most cases put the program in
`t.gp` and run `executable t.gp`; some use stdin or `-e`.
Expected stdout / stderr / exit status (and contents of `check_files`) are
captured from the reference binary by gen_goldens.py.
"""

CASES = []
DUMB = "set term dumb size 79,24\n"


def add(cat, name, argv, stdin="", files=None, check_files=()):
    CASES.append({"id": f"{cat}.{name}", "category": cat, "argv": list(argv), "stdin": stdin,
                  "files": files or {}, "check_files": list(check_files)})


def S(cat, name, script, extra_files=None, check_files=()):
    files = {"t.gp": script}
    files.update(extra_files or {})
    add(cat, name, ["t.gp"], files=files, check_files=check_files)


def T(cat, name, script, **kw):
    """table output: set table to stdout"""
    S(cat, name, "set table\n" + script, **kw)


def D(cat, name, script, size="79,24", **kw):
    """dumb terminal plot"""
    S(cat, name, f"set term dumb size {size}\n" + script, **kw)


DATA1 = "$d << EOD\n1 2.0\n2 4.1\n3 5.9\n4 8.2\n5 9.8\n6 12.3\nEOD\n"
DATA2 = ("$d << EOD\n# x y err\n0 1.0 0.1\n1 2.7 0.2\n2 7.4 0.3\n3 20.1 0.5\n4 54.6 1.0\n\n\n"
         "0 3\n1 2\n2 4\n3 1\n4 5\nEOD\n")
NOISY = "$n << EOD\n" + "".join(f"{x} {((x * 37) % 11) - 5 + 0.5 * x}\n" for x in range(0, 30)) + "EOD\n"
SAMPLE = "$s << EOD\n" + "".join(f"{v}\n" for v in [2.1, 3.5, 3.5, 4.0, 4.2, 5.9, 6.1, 6.1, 6.1, 7.4, 8.8, 9.0, 12.5, 3.3, 4.8]) + "EOD\n"

# ------------------------------------------------------------------ cli
c = "cli"
add(c, "version_long", ["--version"])
add(c, "version_short", ["-V"])
add(c, "help", ["--help"])
add(c, "help_short", ["-h"])
add(c, "unknown_option", ["--bogus"])
add(c, "missing_script", ["nope.gp"])
add(c, "e_multiple", ["-e", "a=2; b=3", "-e", "print a*b"])
add(c, "e_then_file", ["-e", "x=5", "t.gp"], files={"t.gp": "print x**2\n"})
add(c, "file_then_e", ["t.gp", "-e", "print y"], files={"t.gp": "y=7\n"})
add(c, "two_files", ["a.gp", "b.gp"], files={"a.gp": "v = 'from a'\n", "b.gp": "print v . ' and b'\n"})
add(c, "stdin_script", [], stdin="print 'stdin', 1+1\nprint undefined_name\nprint 'not reached'\n")
add(c, "dash_stdin", ["-"], stdin="print 'dash'\n")
add(c, "exit_status", ["t.gp"], files={"t.gp": "print 'a'\nexit status 3\nprint 'b'\n"})
add(c, "exit_error_message", ["t.gp"], files={"t.gp": "print 'a'\nexit error \"custom failure\"\n"})
add(c, "quit_in_middle", ["t.gp"], files={"t.gp": "print 1\nquit\nprint 2\n"})
add(c, "error_stops_script", ["t.gp"], files={"t.gp": "print 1\nprint 1/\nprint 2\n"})
add(c, "e_error_exit", ["-e", "print sin()"])
add(c, "default_settings_flag", ["-d", "t.gp"], files={"t.gp": "show samples\nshow angles\n"})
add(c, "call_with_args", ["-c", "t.gp", "first", "2nd arg", "3"], files={"t.gp": "print ARGC, ARG0, ARG1, ARG2, ARG3\nprint ARGV\n"})
add(c, "persist_ignored", ["-persist", "-e", "print 'ok'"])

# ------------------------------------------------------------------ expressions
c = "expr"
EXPR = {
    "int_arith": "print 7/2, -7/2, 7%3, -7%3, 7.0/2, 2**10, 2**-1, 2.0**-1, -2**2, (-2)**2",
    "int_overflow": "print 2**62, 2**63, 2**64, 9223372036854775807 + 1, -9223372036854775807 - 2, 3037000500**2",
    "float_print_precision": "print 1/3.0, 2/3.0, 1e20, 1e-20, 123456789.123456789, 0.1+0.2, 1e15+0.3, 100.0, 1e300*1e10, -1e300*1e10",
    "nan_inf": "x = 1e308*10\nprint x, -x, x-x, (x-x)==(x-x), x>1e308, sqrt(-1), log(0), log(-1)",
    "division_by_zero": "print 1/0\nprint 1.0/0\nprint 1%0",
    "bit_ops": "print 12 & 10, 12 | 10, 12 ^ 10, ~5, 1 << 4, 256 >> 3, -16 >> 2",
    "logic_and_compare": "print 1 && 0, 1 || 0, !0, !5, 3 > 2, 3 < 2, 2 >= 2, 2 <= 1, 1 == 1.0, 1 != 2, \"a\" eq \"a\", \"a\" ne \"b\"",
    "ternary_and_comma": "x = 5\nprint x > 3 ? \"big\" : \"small\", (a=1, b=2, a+b), x < 3 ? 1 : x < 10 ? 2 : 3",
    "complex_numbers": "z = {3,4}\nprint z, abs(z), real(z), imag(z), arg(z), z*z, z/{0,1}, sqrt({-4,0}), exp({0,pi}), {1,1}**2",
    "string_ops": "s = \"Hello, World\"\nprint s[1:5], s[8:], s[:3], strlen(s), strstrt(s, \"World\"), s . \"!\", substr(s, 3, 4), upper(s), lower(s)",
    "string_number_coercion": "print \"3\" + 4, \"2.5\" * 2, 5 . \"\", \"10\" == 10, \"abc\" + 1",
    "words_and_trim": "s = \"  alpha beta\tgamma  \"\nprint words(s), word(s, 2), word(s, 4), \"[\" . trim(s) . \"]\"",
    "string_functions_more": "print strstrt(\"abc\", \"z\"), sprintf(\"%s-%s\", \"a\", \"b\"), gprintf(\"%.2f\", pi), strlen(\"\"), \"x\"[1:0]",
    "math_functions": "print sin(1), cos(1), tan(1), asin(0.5), acos(0.5), atan(1), atan2(1,-1), sinh(1), cosh(1), tanh(1)",
    "math_functions_2": "print exp(1), log(10), log10(1000), sqrt(2), abs(-3), abs(-3.5), sgn(-2), sgn(0), sgn(4.2)",
    "rounding": "print int(3.7), int(-3.7), floor(-3.5), ceil(-3.5), floor(3), round(2.5), round(-2.5), round(3.49)",
    "special_functions": "print gamma(5), lgamma(10), erf(0.5), erfc(0.5), inverf(0.5), norm(1), invnorm(0.975), besj0(1), besj1(1), besy0(1), besy1(1)",
    "special_functions_2": "print igamma(2, 1), ibeta(2, 3, 0.4), lambertw(1), airy(1), expint(1, 1), voigt(1, 1)",
    "degrees_mode": "set angles degrees\nprint sin(30), cos(60), atan(1), asin(1), atan2(1, 1)\nset angles radians\nprint sin(30)",
    "user_functions": "f(x) = x**2 + 1\ng(x, y) = f(x) * y\nfact(n) = n <= 1 ? 1 : n * fact(n - 1)\nprint f(3), g(2, 3), fact(10), fact(20), fact(21)",
    "function_recursion_depth": "r(n) = n == 0 ? 0 : 1 + r(n-1)\nprint r(100)\nprint r(300000)",
    "variables_and_exists": "a = 1\nprint exists(\"a\"), exists(\"zz\")\nundefine a\nprint exists(\"a\")",
    "sum_operator": "print sum [i=1:10] i, sum [i=1:4] i**2, sum [k=5:1] k, sum [i=1:3] 1.0/i",
    "arrays": "array A[4]\nA[1] = 10; A[2] = \"two\"; A[4] = {1,1}\nprint A\nprint |A|, A[2], A[1] + 1\narray B = [3, 1, 2]\nprint B, B[3]",
    "array_errors": "array A[2]\nprint A[3]",
    "integer_valued_functions": "print int(1e18), int(1e19), int(-0.5), floor(1e10), 7.9 % 2, 2**0, 0**0",
    "rand_reproducible": "print rand(0)\nprint rand(0), rand(0)\nprint rand(42)\nprint rand(0)",
    "time_functions": "print strftime(\"%Y-%m-%d %H:%M:%S\", 0), strftime(\"%j %a %b\", 86400*45.5), strptime(\"%Y-%m-%d\", \"2021-03-04\"), time_tm = 1000000000",
    "time_functions_2": "t = strptime(\"%d/%m/%Y %H:%M\", \"25/12/2020 18:30\")\nprint t, strftime(\"%A %B %d %y %I%p\", t), tm_year(t), tm_mon(t), tm_mday(t), tm_wday(t), tm_yday(t), tm_hour(t)",
    "column_outside_plot": "print column(1)",
    "valid_and_value": "x = 3\nprint value(\"x\"), value(\"x\") * 2",
    "print_many_types": "print 1, 1.0, \"s\", {1,0}, {0,-1.5}, 1e-5, 12345678901234",
    "precedence": "print 2 + 3 * 4 ** 2, -3 ** 2, 2 ** 3 ** 2, 10 - 2 - 3, 100 / 10 / 5, 1 < 2 == 1, !1 + 1",
    "string_compare_numbers": "print \"10\" < \"9\", 10 < 9, \"abc\" eq \"ab\" . \"c\"",
    "factorial_operator": "print 5!, 0!, 20!, 3!!",
    "hex_octal_literals": "print 0x1F, 0X10, 017, 0b101, 1.5e3, .5, 5.",
}
for k, v in EXPR.items():
    S(c, k, v + "\n")

# ------------------------------------------------------------------ control flow / program structure
c = "program"
PROG = {
    "do_for_loop": "do for [i=1:5] {\n  print i, i**2\n}\ndo for [s in \"a bb ccc\"] { print s, strlen(s) }\ndo for [i=10:1:-3] { print i }",
    "while_loop": "n = 0\nwhile (n < 50) { n = n*2 + 1 }\nprint n",
    "if_else_chain": "x = 7\nif (x < 5) { print \"lt5\" } else if (x < 10) { print \"lt10\" } else { print \"big\" }\nif (x) print \"old style\"",
    "break_continue": "do for [i=1:10] {\n  if (i % 2) { continue }\n  if (i > 7) { break }\n  print i\n}",
    "nested_loops": "do for [i=1:3] { do for [j=i:3] { print sprintf(\"%d%d\", i, j) } }",
    "eval_and_macro": "set macros\ncmd = \"print 'evaluated'\"\neval cmd\nv = \"3 + 4\"\nprint @v\nx = @v * 2\nprint x",
    "load_and_call": "print 'main'\nload 'inc.gp'\ncall 'args.gp' 'one' 2 \"three four\"\nprint inc_value",
    "datablock_print": DATA1 + "print $d\nprint |$d|\nprint $d[2]",
    "datablock_redefine_and_undefine": "$x << EOD\na\nEOD\n$x << EOD\nb\nc\nEOD\nprint $x\nundefine $x\nprint exists(\"$x\")",
    "set_print_to_file": "set print 'out.txt'\nprint 'to file', 42\nset print\nprint 'to stderr'\nset print '-'\nprint 'to stdout'",
    "set_print_append": "set print 'out.txt'\nprint 'first'\nset print 'out.txt' append\nprint 'second'\nunset print",
    "set_print_datablock": "set print $buf\nprint 'line 1'\nprint 2, 3\nunset print\nprint $buf\nprint |$buf|",
    "functions_listing": "f(x) = x + 1\ng(a, b) = a * b\nshow functions",
    "variables_listing": "aa = 1\nbb = \"str\"\ncc = 2.5\nshow variables aa\nshow variables bb\nshow variables cc",
    "comments_and_continuation": "# comment\nprint 1 + \\\n  2 # trailing\nprint \"#not a comment\"",
    "multiple_statements_per_line": "a=1; b=2; print a+b; print a-b",
    "string_interpolation_in_set": "t = 'My Title'\nset title t\nshow title",
    "iteration_in_print": "print sum [i=1:3] i, 1",
    "error_inside_loop": "do for [i=1:5] {\n  print i\n  if (i == 3) { print undefined_var }\n}",
    "error_inside_load": "print 'before'\nload 'bad.gp'\nprint 'after'",
    "reread_and_pause": "pause 0\npause 0 'message shown'\nprint 'ok'",
    "evaluate_with_reset": "set samples 7\nreset\nshow samples",
}
EXTRA = {
    "load_and_call": {"inc.gp": "inc_value = 99\nprint 'inside inc'\n", "args.gp": "print 'ARGC=', ARGC\nprint ARG1, ARG2, ARG3\nprint ARG0\n"},
    "error_inside_load": {"bad.gp": "print 'in bad'\nset xrange [1:\n"},
}
CHECK = {"set_print_to_file": ["out.txt"], "set_print_append": ["out.txt"]}
for k, v in PROG.items():
    S(c, k, v + "\n", extra_files=EXTRA.get(k), check_files=CHECK.get(k, ()))

# ------------------------------------------------------------------ sprintf / gprintf
c = "format"
FMT = {
    "sprintf_ints": 'print sprintf("[%d] [%5d] [%-5d] [%05d] [%+d] [%x] [%X] [%o] [%#x]", 42, 42, 42, 42, 42, 255, 255, 8, 255)',
    "sprintf_floats": 'print sprintf("[%f] [%.2f] [%10.3f] [%-10.1f] [%e] [%.3E] [%g] [%G] [%.3g]", pi, pi, pi, pi, 12345.678, 0.000123, 1e-5, 1e20, 1234.5)',
    "sprintf_strings": 'print sprintf("[%s] [%10s] [%-10s] [%.2s] [%%]", "abc", "abc", "abc", "abc")',
    "sprintf_type_coercion": 'print sprintf("%d %f %s", 3.9, 2, 7)\nprint sprintf("%d", "12")',
    "sprintf_errors_too_few": 'print sprintf("%d %d", 1)',
    "sprintf_errors_bad": 'print sprintf("%s", 1)',
    "sprintf_many": 'print sprintf("%s=%d;%s=%.1f", "a", 1, "b", 2.25)',
    "gprintf_basic": 'print gprintf("%g", 1234.5), gprintf("%.3f", 2), gprintf("%t", 1234.5), gprintf("%T", 1234.5), gprintf("%l", 1234.5), gprintf("%L", 1234.5)',
    "gprintf_mantissa_exponent": 'do for [v in "0.000123 1 999 1e6 2.5e-9 -42"] { print gprintf("%.2t x 10^%T", v+0), gprintf("%s%c", v+0), gprintf("%.1s %c", v+0) }',
    "gprintf_pi_and_binary": 'print gprintf("%P", pi), gprintf("%.2P", 2.5*pi), gprintf("%b", 4096), gprintf("%B", 4096), gprintf("%h", 1e-5)',
    "gprintf_combined": 'print gprintf("value: %5.2f units", 3.14159), gprintf("%x", 255), gprintf("%o", 8)',
    "print_default_format": 'print 1.0, 0.1, 1e6, 1e16, 1e17, 123456.7, 1234567.8, 0.00012345, 3.0e-7',
    "format_command_and_show": 'set format x "%.2f"\nset format y "%g units"\nset format z "%t"\nshow format',
    "set_decimalsign": 'set decimalsign ","\nprint gprintf("%.3f", pi)\nprint sprintf("%.3f", pi)',
}
for k, v in FMT.items():
    S(c, k, v + "\n")

# ------------------------------------------------------------------ errors
c = "errors"
ERR = {
    "invalid_expression": "print 1 +",
    "unbalanced_paren": "print (1 + 2",
    "undefined_function": "print nosuch(1)",
    "wrong_arg_count": "f(x) = x\nprint f(1, 2)",
    "builtin_wrong_args": "print sin(1, 2)",
    "string_arith": "print \"abc\" * 2",
    "unknown_command": "frobnicate the plot",
    "unknown_set_option": "set nosuchoption",
    "bad_range": "set xrange [5:",
    "bad_range_2": "set xrange [a:b]",
    "plot_nothing": "plot",
    "plot_undefined_function": "set table\nplot zzz(x)",
    "plot_missing_datablock": "set table\nplot $nothere",
    "plot_missing_file": "set table\nplot 'nonexistent.dat'",
    "bad_using": DATA1 + "set table\nplot $d using 1:(",
    "column_out_of_range": DATA1 + "set table\nplot $d using 1:5",
    "empty_range": "set table\nset xrange [1:1]\nplot x",
    "log_negative_range": "set table\nset logscale y\nset yrange [-1:10]\nplot x",
    "set_terminal_unknown": "set terminal nosuchterm",
    "set_samples_invalid": "set samples 1",
    "fit_no_params": DATA1 + "fit a*x $d",
    "fit_undefined_function": DATA1 + "fit q(x) $d via a",
    "do_for_bad": "do for [i=1:] { print i }",
    "error_line_numbers": "\n\nx = 1\n\nprint x +* 2\n",
    "error_with_long_line": "print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 27",
    "missing_quote": "print \"unterminated",
    "array_bad_index": "array A[3]\nA[0] = 1",
    "array_not_array": "x = 1\nprint x[1]",
    "datablock_unterminated": "$d << EOD\n1 2\n",
    "stats_no_data": "stats $nope",
    "bad_format_in_gprintf": "print gprintf(\"%d %d\", 1)",
    "unset_unknown": "unset bogus",
    "show_unknown": "show nothinghere",
    "undefined_in_function_body": "f(x) = x + undefined_y\nprint f(1)",
    "type_error_bitwise": "print 1.5 & 3",
    "type_error_modulo_float": "print 5.5 % 2",
    "string_index_error": "print \"abc\"[0:1]",
    "warning_continues": "set term dumb size 79,24\nset logscale x\nset xrange [-1:10]\nprint 'still running'",
}
for k, v in ERR.items():
    S(c, k, v + "\n")
add(c, "error_from_e_flag", ["-e", "set xrange [1:", "-e", "print 2"])
add(c, "error_from_stdin_line", [], stdin="print 1\n\nprint 2 +\nprint 3\n")

# ------------------------------------------------------------------ show / set state
c = "show"
SHOW = [
    "xrange", "yrange", "samples", "angles", "style data", "style function", "key", "border", "logscale",
    "xtics", "ytics", "mxtics", "grid", "title", "xlabel", "size", "origin", "margin", "datafile", "zero",
    "clip", "offsets", "isosamples", "view", "palette", "colorbox", "boxwidth", "style line", "dummy", "encoding",
    "timefmt", "xdata", "fit", "loadpath", "bars", "pointsize", "polar", "parametric", "contour", "hidden3d",
    "minussign", "decimalsign", "tics", "autoscale", "jitter", "errorbars",
]
for opt in SHOW:
    S(c, "default_" + opt.replace(" ", "_"), f"show {opt}\n")
SHOWSET = {
    "xrange_set": "set xrange [-2.5:10]\nshow xrange\nset xrange [*:5] reverse\nshow xrange",
    "key_set": "set key top left box title 'Legend' font ',10' spacing 1.5\nshow key\nunset key\nshow key",
    "logscale_set": "set logscale xy 2\nset logscale z\nshow logscale\nunset logscale y\nshow logscale",
    "tics_set": "set xtics 0, 0.5, 3 rotate by 45 nomirror out\nset ytics ('low' 0, 'mid' 5, 'high' 10)\nshow xtics\nshow ytics",
    "label_set": "set label 1 'first' at 1,2 center\nset label 'second' at graph 0.5,0.5 right rotate by 90\nset label 3 'x' at screen 0.1, second 2 front tc rgb 'red'\nshow label",
    "arrow_set": "set arrow from 0,0 to 1,1\nset arrow 5 from graph 0,0 rto 1,2 nohead lw 2 dt 2\nshow arrow",
    "style_line_set": "set style line 1 lc rgb '#ff0000' lw 2 pt 7 ps 1.5\nset style line 2 lt 3 dashtype '--'\nshow style line",
    "grid_set": "set grid xtics mytics lt 0 lw 1, lt 2\nshow grid",
    "margins_set": "set lmargin 5\nset rmargin at screen 0.9\nset tmargin 0\nshow margin",
    "multiple_ranges": "set xrange [1:2]; set yrange [3:4]; set y2range [5:6]; set cbrange [7:8]\nshow xrange\nshow yrange\nshow y2range\nshow cbrange",
    "timefmt_set": "set xdata time\nset timefmt '%Y-%m-%d'\nset format x '%b %d'\nshow xdata\nshow timefmt\nshow format",
    "datafile_set": "set datafile separator ','\nset datafile missing 'NaN'\nset datafile commentschars '#!'\nshow datafile",
    "samples_isosamples": "set samples 50, 60\nset isosamples 12\nshow samples\nshow isosamples",
    "reset_restores": "set xrange [1:2]\nset samples 10\nset key off\nreset\nshow xrange\nshow samples\nshow key",
    "save_settings_subset": "set xrange [0:5]\nset title 'T'\nshow title\nshow xrange",
    "show_all_style": "set style data linespoints\nset style function impulses\nset style fill solid 0.5 border -1\nshow style",
    "boxwidth_set": "set boxwidth 0.8 relative\nshow boxwidth\nset boxwidth 2 absolute\nshow boxwidth",
    "view_set": "set view 30, 120, 1.2, 0.8\nshow view\nset view map\nshow view",
    "unset_and_show": "unset border\nunset xtics\nunset title\nshow border\nshow xtics\nshow title",
}
for k, v in SHOWSET.items():
    S(c, k, v + "\n")

# ------------------------------------------------------------------ table output (sampling, data handling)
c = "table"
TAB = {
    "function_default_samples": "plot sin(x)",
    "function_samples_range": "set samples 11\nset xrange [0:1]\nplot x**2, 1-x",
    "two_functions_titles": "set samples 5\nplot [0:4] x title 'line', x**2 notitle",
    "undefined_points": "set samples 9\nplot [-2:2] sqrt(x), 1/x",
    "log_x_sampling": "set samples 8\nset logscale x\nplot [1:1000] log10(x)",
    "data_basic": DATA1 + "plot $d",
    "data_using_expressions": DATA1 + "plot $d using 1:($2*2), '' using ($1+0.5):(sqrt($2)) title 'sqrt'",
    "data_using_column_functions": DATA1 + "plot $d using 0:2, $d using (column(0)):(valid(2) ? $2 : 1/0), $d using 1:(stringcolumn(1).'x')",
    "data_every": DATA1 + "plot $d every 2, $d every ::2::4",
    "data_index_blocks": DATA2 + "plot $d index 0 using 1:2, $d index 1",
    "data_with_errorbars": DATA2 + "plot $d index 0 using 1:2:3 with yerrorbars",
    "data_missing_and_comments": "$m << EOD\n# header\n1 1\n2 ?\n3 NaN\n\n4 4\n5 abc\n6 6\nEOD\nset datafile missing '?'\nplot $m",
    "csv_separator": "$c << EOD\nx,y,z\n1,2,3\n4,,6\n7,8,9\nEOD\nset datafile separator comma\nplot $c using 1:3, $c using 1:2",
    "columnheader": "$c << EOD\nname value other\n1 10 100\n2 20 200\nEOD\nplot $c using 1:2 title columnheader, $c using 1:3 title columnheader(3)",
    "named_columns": "$c << EOD\nalpha beta\n1 10\n2 20\nEOD\nset key autotitle columnhead\nplot $c using 'alpha':'beta'",
    "time_data": "$t << EOD\n2020-01-01 5\n2020-01-15 7\n2020-03-01 2\nEOD\nset xdata time\nset timefmt '%Y-%m-%d'\nset format x '%d/%m'\nplot $t using 1:2",
    "table_to_datablock": "set table $out\nset samples 4\nplot [0:3] x*x\nunset table\nprint $out\nprint |$out|",
    "table_with_table_style": DATA1 + "plot $d using 1:2:($1*$2) with table",
    "table_with_table_format": DATA1 + "set table separator comma\nplot $d using 1:($2/3) with table",
    "splot_function": "set isosamples 3\nset samples 3\nsplot [0:1][0:1] x+y",
    "splot_data": "$g << EOD\n0 0 1\n0 1 2\n\n1 0 3\n1 1 4\nEOD\nsplot $g using 1:2:3",
    "parametric": "set parametric\nset samples 5\nplot [0:pi] cos(t), sin(t)",
    "polar": "set polar\nset samples 5\nplot [0:pi] 1",
    "iteration_plot": "set samples 3\nplot [0:2] for [n=1:3] x**n title sprintf('n=%d', n)",
    "histogram_style_table": "$h << EOD\nA 3 4\nB 5 1\nC 2 6\nEOD\nset style data histograms\nplot $h using 2:xtic(1), '' using 3",
    "boxes_and_steps": DATA1 + "plot $d with boxes, $d with steps, $d with fsteps",
    "filledcurves_table": DATA1 + "plot $d using 1:2:($2+1) with filledcurves",
    "ranges_clip_data": DATA1 + "set xrange [2:4.5]\nplot $d",
    "autoscale_extend_table": "set samples 4\nplot [-1:1] 3*x",
    "x2_y2_axes": DATA1 + "plot $d axes x2y2, $d using 1:($2*10) axes x1y2",
    "sample_keyword": "plot sample [0:1:0.25] x, [2:3:0.5] x**2",
    "dummy_variable": "set dummy u\nset samples 3\nplot [0:2] u**3",
    "binary_operators_in_using": DATA1 + "plot $d using 1:($2 > 5 ? $2 : NaN)",
    "array_plot": "array A = [5, 3, 8]\nplot A, A using 1:(A[$1]*2)",
    "string_column_xtic": "$h << EOD\nmon 1\ntue 3\nwed 2\nEOD\nplot $h using 0:2:xtic(1) with table",
}
for k, v in TAB.items():
    T(c, k, v + "\n")

# ------------------------------------------------------------------ smoothing / binning algorithms
c = "smooth"
for m in ["unique", "frequency", "fnormal", "cumulative", "cnormal", "csplines", "acsplines", "mcsplines", "bezier", "sbezier", "kdensity", "path"]:
    using = "1:2:(1)" if m == "acsplines" else "1:2"
    T(c, m, NOISY + f"set samples 15\nplot $n using {using} smooth {m}\n")
T(c, "unique_averages_duplicates", "$u << EOD\n3 1\n1 2\n3 5\n2 2\n1 4\nEOD\nplot $u smooth unique, $u smooth frequency\n")
T(c, "kdensity_bandwidth", SAMPLE + "set samples 12\nplot $s using 1:(1) smooth kdensity bandwidth 0.7, $s using 1:(1) smooth kdensity\n")
T(c, "kdensity_period", SAMPLE + "set samples 10\nplot $s using 1:(1) smooth kdensity bandwidth 1.0 period 6\n")
T(c, "bins", SAMPLE + "plot $s using 1:(1) bins=5, $s using 1:(1) bins binwidth=2 binrange [0:14]\n")
T(c, "acsplines_weights", DATA1 + "set samples 10\nplot $d using 1:2:(1e-3) smooth acsplines, $d using 1:2:(100) smooth acsplines\n")
T(c, "csplines_two_points", "$p << EOD\n0 0\n1 1\nEOD\nset samples 5\nplot $p smooth csplines\n")
T(c, "cumulative_normalized", SAMPLE + "plot $s using 1:(1) smooth cnormal, $s using 1:(1) smooth cumulative\n")
T(c, "bezier_samples", DATA1 + "set samples 7\nplot $d smooth bezier, $d smooth sbezier\n")
T(c, "smooth_with_log", DATA1 + "set logscale y\nset samples 6\nplot $d smooth csplines\n")
T(c, "zsort_and_convexhull", "$p << EOD\n0 0\n2 0\n1 1\n2 2\n0 2\n1 3\nEOD\nplot $p smooth convexhull, $p using 1:2:(-$2) smooth zsort\n")
T(c, "unwrap", "$p << EOD\n0 3.0\n1 -3.0\n2 3.1\n3 -2.9\nEOD\nplot $p smooth unwrap\n")
T(c, "mcsplines_monotone", "$p << EOD\n0 0\n1 0\n2 1\n3 1\n4 5\nEOD\nset samples 9\nplot $p smooth mcsplines\n")

# ------------------------------------------------------------------ stats
c = "stats"
S(c, "two_columns", DATA1 + "stats $d\n")
S(c, "single_column", SAMPLE + "stats $s\n")
S(c, "named_prefix_variables", DATA1 + "stats $d using 2 name 'Y' nooutput\nprint Y_mean, Y_stddev, Y_min, Y_max, Y_median, Y_records, Y_sum, Y_lo_quartile, Y_up_quartile\n")
S(c, "default_variables", DATA1 + "stats $d nooutput\nprint STATS_correlation, STATS_slope, STATS_intercept, STATS_mean_x, STATS_mean_y, STATS_sumxy, STATS_pos_max_y\n")
S(c, "multiple_blocks", DATA2 + "stats $d\n")
S(c, "index_and_every", DATA2 + "stats $d index 1 every 2 using 2\n")
S(c, "with_missing_and_invalid", "$m << EOD\n1 2\n2 ?\n3 x\n4 8\n\n5 10\nEOD\nset datafile missing '?'\nstats $m\n")
S(c, "range_restricted", DATA1 + "stats [2:5] $d using 1:2\n")
S(c, "matrix", "$m << EOD\n1 2 3\n4 5 6\nEOD\nstats $m matrix\n")
S(c, "expression_columns", DATA1 + "stats $d using ($1*2):(log($2))\n")
S(c, "noisy_data", NOISY + "stats $n\n")
S(c, "show_variables_after", DATA1 + "stats $d using 1 nooutput\nshow variables STATS_\n")
S(c, "output_to_print_file", DATA1 + "set print 'stats.txt'\nstats $d\nset print\nprint 'done'\n", check_files=["stats.txt"])

# ------------------------------------------------------------------ fit
c = "fit"
S(c, "linear", DATA1 + "f(x) = a*x + b\nfit f(x) $d via a, b\n")
S(c, "quadratic_quiet", DATA1 + "set fit quiet\nf(x) = a*x**2 + b*x + c\nfit f(x) $d via a, b, c\nprint a, b, c\nprint FIT_NDF, FIT_WSSR, FIT_STDFIT, FIT_CONVERGED\n")
S(c, "exponential_with_errors", DATA2 + "set fit logfile 'my.log'\ng(x) = A*exp(k*x)\nA = 1; k = 1\nfit g(x) $d index 0 using 1:2:3 yerrors via A, k\n")
S(c, "brief_errorvariables", DATA1 + "set fit brief errorvariables nolog\nfit m*x + q $d via m, q\nprint m, m_err, q, q_err\n")
S(c, "verbose", DATA1 + "set fit verbose nolog\nfit m*x $d via m\n")
S(c, "limits_and_start", NOISY + "set fit nolog quiet limit 1e-9 maxiter 50 start_lambda 0.1 lambda_factor 5\nfit p*x + r $n via p, r\nprint p, r, FIT_CONVERGED, FIT_NITER\n")
S(c, "maxiter_hit", NOISY + "set fit nolog maxiter 2\nh(x) = a*sin(b*x) + c\na=5; b=1; c=0\nfit h(x) $n via a, b, c\n")
S(c, "fit_ranges", DATA1 + "set fit nolog\nfit [2:5] a*x + b $d via a, b\n")
S(c, "fixed_parameter_file", DATA1 + "set fit nolog\nfit a*x + b $d via 'start.par'\nprint a, b\n", extra_files={"start.par": "a = 2\nb = 0.5 # FIXED\n"})
S(c, "covariance_variables", DATA1 + "set fit quiet nolog covariancevariables\nfit a*x + b $d via a, b\nprint FIT_COV_a_b, FIT_COV_a_a\n")
S(c, "two_dimensional", "$g << EOD\n0 0 1\n0 1 3\n1 0 2\n1 1 4.2\n2 1 5.1\n2 2 7\nEOD\nset fit nolog\nfit a*x + b*y + c $g using 1:2:3:(1) via a, b, c\n")
S(c, "singular_fit", "$z << EOD\n1 1\n1 1\n1 1\nEOD\nset fit nolog\nfit a*x + b $z via a, b\n")
S(c, "update_file", DATA1 + "set fit nolog quiet\na = 1; b = 1\nfit a*x + b $d via a, b\nupdate 'p.par'\n", check_files=["p.par"])

# ------------------------------------------------------------------ dumb terminal plots
c = "dumb"
DPLOTS = {
    "sin_default": "plot sin(x)",
    "two_functions": "plot [-5:5] x**2/5, abs(x) title 'abs'",
    "small_canvas": ("plot cos(x)", "40,12"),
    "wide_canvas": ("plot [0:20] sin(x)*x", "120,30"),
    "data_points": DATA1 + "plot $d with points",
    "data_linespoints": DATA1 + "plot $d with linespoints title 'measurements'",
    "impulses": DATA1 + "plot $d with impulses",
    "boxes": DATA1 + "set boxwidth 0.5\nset style fill solid\nplot $d with boxes",
    "histogram": "$h << EOD\nA 3 4\nB 5 1\nC 2 6\nEOD\nset style data histograms\nset style histogram clustered\nplot $h using 2:xtic(1) title 'one', '' using 3 title 'two'",
    "steps": DATA1 + "plot $d with steps",
    "errorbars": DATA2 + "plot $d index 0 using 1:2:3 with yerrorbars",
    "title_labels": "set title 'Main Title'\nset xlabel 'time (s)'\nset ylabel 'amplitude'\nplot sin(x)",
    "key_positions": "set key left bottom\nplot [0:5] x, 5-x",
    "key_outside_box": "set key outside right box\nplot [0:5] x, 5-x",
    "no_key_no_border": "unset key\nunset border\nplot [0:3] x**2",
    "grid": "set grid\nplot [0:10] sqrt(x)",
    "custom_tics": "set xtics 0, 2, 10\nset ytics ('lo' -1, 'zero' 0, 'hi' 1)\nplot [0:10] sin(x)",
    "mirror_off_and_out": "set xtics nomirror out\nset ytics nomirror\nplot [0:6] exp(-x)",
    "log_scale": "set logscale y\nplot [1:100] x**2",
    "log_both": "set logscale xy\nplot [1:1000] x**1.5",
    "yrange_fixed": "set yrange [-2:2]\nplot tan(x)",
    "negative_ranges": "plot [-100:-10] x",
    "tiny_values": "plot [0:1e-6] x*1e-6",
    "huge_values": "plot [0:1e9] x**2",
    "format_tics": "set format y '%.1e'\nset format x '%.0f%%'\nplot [0:100] x/3",
    "time_axis": "$t << EOD\n2021-01-01 1\n2021-02-01 4\n2021-03-01 2\n2021-04-01 5\nEOD\nset xdata time\nset timefmt '%Y-%m-%d'\nset format x '%b'\nplot $t using 1:2 with linespoints",
    "labels_and_arrows": "set label 'peak' at 1.57,1\nset arrow from 0,0 to 3,0.5\nplot [0:3.14] sin(x)",
    "multiplot_layout": "set multiplot layout 1,2 title 'two'\nplot [0:3] x\nplot [0:3] -x\nunset multiplot",
    "parametric_circle": "set parametric\nset size ratio -1\nplot [0:2*pi] cos(t), sin(t)",
    "polar_plot": "set polar\nplot [0:2*pi] 1+cos(t)",
    "zero_axis": "set xzeroaxis\nset yzeroaxis\nplot [-3:3] x**3/10",
    "y2_axis": DATA1 + "set y2tics\nplot $d axes x1y1, $d using 1:($2*100) axes x1y2",
    "filledcurves": "plot [0:3] x with filledcurves y=0",
    "splot_surface": "set isosamples 10\nsplot x*y",
    "splot_hidden3d": "set hidden3d\nset isosamples 15\nsplot [-2:2][-2:2] exp(-x**2-y**2)",
    "splot_view_map": "set view map\nset isosamples 8\nsplot x+y",
    "contour": "set contour base\nset cntrparam levels 3\nunset surface\nset view map\nsplot [-2:2][-2:2] x**2+y**2",
    "dumb_options_aspect": ("plot [0:1] x", "50,20 aspect 1,1"),
    "dumb_noenhanced_feed": ("set title 'x_{sub}^2'\nplot [0:1] x", "60,18 noenhanced nofeed"),
    "point_types": DATA1 + "plot $d using 1:2 with points pt 1, '' using 1:($2-2) with points pt 6",
    "replot": "plot [0:2] x\nreplot x**2",
    "datafile_columns_plot": "$c << EOD\nx a b\n1 1 3\n2 4 2\n3 9 1\nEOD\nset key autotitle columnhead\nplot for [i=2:3] $c using 1:i with lines",
    "set_output_file": "set output 'plot.txt'\nplot [0:1] x\nset output\nprint 'written'",
}
for k, v in DPLOTS.items():
    script, size = (v if isinstance(v, tuple) else (v, "79,24"))
    D(c, k, script + "\n", size=size, check_files=["plot.txt"] if k == "set_output_file" else ())

# ------------------------------------------------------------------ other text terminals
c = "terminals"
S(c, "svg_simple", "set term svg size 300,200\nplot [0:1] x\n")
S(c, "svg_with_text", "set term svg size 200,150 font 'Arial,10'\nset title 'Hello & <World>'\nplot [0:1] x**2 title 'quad'\n")
S(c, "canvas_simple", "set term canvas size 200,100\nplot [0:1] x\n")
S(c, "postscript_header_tail", "set term postscript eps\nset output 'p.eps'\nplot [0:1] x\nset output\nprint 'done'\n")
S(c, "show_terminal_dumb", "set term dumb size 60,20 ansi\nshow terminal\n")
S(c, "unknown_terminal_option", "set term dumb bogus\n")
S(c, "term_list", "set term dumb\nshow term\nset term push\nset term svg\nset term pop\nshow term\n")



# ------------------------------------------------------------------ generated breadth: dumb plots
FUNCS = {
    "poly": "x**3 - 3*x",
    "gauss": "exp(-x**2)",
    "sinc": "x == 0 ? 1 : sin(3*x)/(3*x)",
    "abs_saw": "abs(x - floor(x) - 0.5)",
    "step": "x < 0 ? -1 : 1",
    "lin": "0.5*x + 1",
    "atan": "atan(2*x)",
    "cosh": "cosh(x)/10",
}
VARIANTS = {
    "plain": ("set xrange [-2:2]\n", "79,24"),
    "narrow": ("set xrange [-2:2]\n", "45,16"),
    "tall": ("set xrange [-2:2]\n", "60,40"),
    "samples20_points": ("set xrange [-2:2]\nset samples 20\nset style function points\n", "79,24"),
    "noborder_keyleft": ("set xrange [-3:1]\nunset border\nset key left top\nset xtics axis\nset ytics axis\n", "70,22"),
    "yrange_grid": ("set xrange [-2:2]\nset yrange [-1.5:1.5]\nset grid\nset tics out\n", "79,24"),
    "impulses_s15": ("set xrange [-2:2]\nset samples 15\nset style function impulses\n", "79,24"),
}
for fname, f in FUNCS.items():
    for vname, (setup, size) in VARIANTS.items():
        D("dumb_matrix", f"{fname}__{vname}", setup + f"plot {f} title '{fname}'\n", size=size)

# ------------------------------------------------------------------ generated breadth: table sampling
for fname, f in FUNCS.items():
    T("table_matrix", f"{fname}__s7", f"set samples 7\nplot [-2:2] {f}\n")
    T("table_matrix", f"{fname}__log", f"set samples 6\nset logscale x\nplot [0.1:10] {f}\n")
    T("table_matrix", f"{fname}__y_restricted", f"set samples 9\nset yrange [-0.5:0.5]\nplot [-2:2] {f}\n")

# ------------------------------------------------------------------ generated breadth: expression printing
EXPRS = [
    "1/7.0", "2**0.5", "10**15/3.0", "1e-7*3", "-0.0", "1e100", "123456789012", "2.0**53", "2.0**53+1", "(2**31)*2",
    "7.0/3*3", "exp(10)", "exp(-10)", "log(2)*1e6", "pi*1e-3", "1.0/3e5", "sqrt(1e-30)", "100.0/7", "1e16/3",
    "int(2.5e9)", "0.1*3", "13 % -4", "-13 % 4", "-13 / 4", "13 / -4", "2**-3", "2**63-1", "-2**63", "5 ** -1", "10**-2",
]
for i, e in enumerate(EXPRS):
    S("expr_print", f"e{i:02d}", f"print {e}\nprint sprintf('%.17g', {e})\n")

# ------------------------------------------------------------------ difficulty tuning (round 2): deeper algorithmic surface
# keep the cheap expression-printing block smaller
CASES[:] = [c for c in CASES if not (c["category"] == "expr_print" and int(c["id"].split(".e")[1]) % 2)]

SURF = {"saddle": "x**2 - y**2", "bump": "exp(-(x**2+y**2))", "ripple": "sin(x)*cos(y)", "plane": "x + 2*y"}
SVIEWS = {
    "default": "",
    "view_60_30": "set view 60, 30\n",
    "hidden3d": "set hidden3d\n",
    "map_contour": "set view map\nset contour base\nset cntrparam levels 4\nunset surface\n",
    "ticslevel0_iso6": "set ticslevel 0\nset isosamples 6\n",
}
for sn, f in SURF.items():
    for vn, setup in SVIEWS.items():
        D("dumb3d", f"{sn}__{vn}", "set isosamples 10\n" + setup + f"splot [-2:2][-2:2] {f} title '{sn}'\n")
for sn, f in SURF.items():
    T("table3d", f"{sn}__grid", f"set isosamples 4, 3\nsplot [-1:1][-1:1] {f}\n")
    T("table3d", f"{sn}__contour", f"set contour base\nset cntrparam levels 3\nunset surface\nset isosamples 8\nsplot [-2:2][-2:2] {f}\n")
    T("table3d", f"{sn}__dgrid3d", "$p << EOD\n0 0 1\n1 0 2\n0 1 3\n1 1 1\n0.5 0.5 5\nEOD\nset dgrid3d 4,4\n" + "splot $p\n" if sn == "saddle" else f"set isosamples 3\nset samples 3\nsplot [0:2][0:2] {f} with points\n")

for i, (layout, plots) in enumerate([
    ("2,1", ["sin(x)", "cos(x)"]), ("2,2", ["x", "x**2", "-x", "abs(x)"]), ("1,3 title 'three'", ["1", "x", "x**3"]),
    ("2,2 rowsfirst downwards", ["x", "2*x", "3*x"]), ("2,1 margins 0.1,0.9,0.1,0.9 spacing 0.05", ["exp(x)", "log(abs(x)+1)"])]):
    D("multiplot", f"layout_{i}", f"set multiplot layout {layout}\n" + "".join(f"plot [-2:2] {p}\n" for p in plots) + "unset multiplot\n", size="90,30")
D("multiplot", "manual_size_origin", "set multiplot\nset size 0.5,0.5\nset origin 0,0\nplot [0:1] x\nset origin 0.5,0.5\nplot [0:1] 1-x\nunset multiplot\n", size="80,30")

for name, script in {
    "basic_lines": "plot [0:1] x, x**2",
    "points_and_key": "$d << EOD\n1 1\n2 3\n3 2\nEOD\nset key left\nplot $d with points pt 7 title 'pts'",
    "title_labels": "set title 'T'\nset xlabel 'X axis'\nset ylabel 'Y'\nplot [0:2] sin(x)",
    "boxes_fill": "$d << EOD\n1 1\n2 3\n3 2\nEOD\nset style fill solid 0.5\nplot $d with boxes",
    "logscale_grid": "set logscale y\nset grid\nplot [1:10] exp(x)",
    "dashed_colors": "plot [0:1] x lc rgb 'red' dt 2, x**2 lc rgb '#00ff00' lw 3",
}.items():
    S("svg", name, "set term svg size 320,240 font 'Sans,10'\n" + script + "\n")

for i, (model, init) in enumerate([("a*x + b", ""), ("a*exp(b*x)", "a=1; b=0.3\n"), ("a*x**2 + b*x + c", ""),
                                   ("a/(1+exp(-b*(x-c)))", "a=12; b=1; c=3\n"), ("a*log(x) + b", ""), ("a*sin(b*x) + c*x", "a=1; b=1; c=2\n")]):
    S("fit_matrix", f"model{i}", DATA1 + f"set fit nolog\n{init}fit {model} $d via " + ",".join(sorted({p for p in 'abc' if p in model})) + "\n")
    S("fit_matrix", f"model{i}_noisy", NOISY + f"set fit nolog quiet\n{init}fit {model} $n via " + ",".join(sorted({p for p in 'abc' if p in model})) + "\nprint a, b, FIT_WSSR\n")

for m in ["csplines", "acsplines", "mcsplines", "bezier", "sbezier", "kdensity", "cumulative", "cnormal", "unique", "frequency", "fnormal"]:
    using = "1:2:(1)" if m == "acsplines" else ("1:(1)" if m in ("kdensity",) else "1:2")
    T("smooth_matrix", m + "_sample", SAMPLE.replace("$s <<", "$s <<") + "$q << EOD\n" + "".join(f"{i} {v}\n" for i, v in enumerate([2.1, 3.5, 3.5, 4.0, 4.2, 5.9, 6.1, 6.1, 6.1, 7.4])) + "EOD\n" + f"set samples 9\nplot $q using {using} smooth {m}\n")
    T("smooth_matrix", m + "_xrange", NOISY + f"set samples 8\nset xrange [5:20]\nplot $n using {using} smooth {m}\n")

for i, opts in enumerate(["using 2", "using 1:2", "using ($1/2):($2*$2)", "using 2 prefix 'P'", "[0:10] using 1:2", "every ::3 using 2"]):
    S("stats_matrix", f"s{i}", NOISY + f"stats $n {opts}\n")

if __name__ == "__main__":
    from collections import Counter
    print(len(CASES), Counter(c["category"] for c in CASES))
