"""Behavioural tests: program (22 cases, golden outputs in golden/program.json)."""
from eval.tests._harness import check


def test_do_for_loop():
    """argv: ['t.gp']
    t.gp:
        do for [i=1:5] {
          print i, i**2
        }
        do for [s in "a bb ccc"] { print s, strlen(s) }
        do for [i=10:1:-3] { print i }
    """
    check("program.do_for_loop")


def test_while_loop():
    """argv: ['t.gp']
    t.gp:
        n = 0
        while (n < 50) { n = n*2 + 1 }
        print n
    """
    check("program.while_loop")


def test_if_else_chain():
    """argv: ['t.gp']
    t.gp:
        x = 7
        if (x < 5) { print "lt5" } else if (x < 10) { print "lt10" } else { print "big" }
        if (x) print "old style"
    """
    check("program.if_else_chain")


def test_break_continue():
    """argv: ['t.gp']
    t.gp:
        do for [i=1:10] {
          if (i % 2) { continue }
          if (i > 7) { break }
          print i
        }
    """
    check("program.break_continue")


def test_nested_loops():
    """argv: ['t.gp']
    t.gp:
        do for [i=1:3] { do for [j=i:3] { print sprintf("%d%d", i, j) } }
    """
    check("program.nested_loops")


def test_eval_and_macro():
    """argv: ['t.gp']
    t.gp:
        set macros
        cmd = "print 'evaluated'"
        eval cmd
        v = "3 + 4"
        print @v
        x = @v * 2
        print x
    """
    check("program.eval_and_macro")


def test_load_and_call():
    """argv: ['t.gp']
    t.gp:
        print 'main'
        load 'inc.gp'
        call 'args.gp' 'one' 2 "three four"
        print inc_value
    """
    check("program.load_and_call")


def test_datablock_print():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        print $d
        print |$d|
        print $d[2]
    """
    check("program.datablock_print")


def test_datablock_redefine_and_undefine():
    """argv: ['t.gp']
    t.gp:
        $x << EOD
        a
        EOD
        $x << EOD
        b
        c
        EOD
        print $x
        undefine $x
        print exists("$x")
    """
    check("program.datablock_redefine_and_undefine")


def test_set_print_to_file():
    """argv: ['t.gp']
    t.gp:
        set print 'out.txt'
        print 'to file', 42
        set print
        print 'to stderr'
        set print '-'
        print 'to stdout'
    """
    check("program.set_print_to_file")


def test_set_print_append():
    """argv: ['t.gp']
    t.gp:
        set print 'out.txt'
        print 'first'
        set print 'out.txt' append
        print 'second'
        unset print
    """
    check("program.set_print_append")


def test_set_print_datablock():
    """argv: ['t.gp']
    t.gp:
        set print $buf
        print 'line 1'
        print 2, 3
        unset print
        print $buf
        print |$buf|
    """
    check("program.set_print_datablock")


def test_functions_listing():
    """argv: ['t.gp']
    t.gp:
        f(x) = x + 1
        g(a, b) = a * b
        show functions
    """
    check("program.functions_listing")


def test_variables_listing():
    """argv: ['t.gp']
    t.gp:
        aa = 1
        bb = "str"
        cc = 2.5
        show variables aa
        show variables bb
        show variables cc
    """
    check("program.variables_listing")


def test_comments_and_continuation():
    """argv: ['t.gp']
    t.gp:
        # comment
        print 1 + \\
          2 # trailing
        print "#not a comment"
    """
    check("program.comments_and_continuation")


def test_multiple_statements_per_line():
    """argv: ['t.gp']
    t.gp:
        a=1; b=2; print a+b; print a-b
    """
    check("program.multiple_statements_per_line")


def test_string_interpolation_in_set():
    """argv: ['t.gp']
    t.gp:
        t = 'My Title'
        set title t
        show title
    """
    check("program.string_interpolation_in_set")


def test_iteration_in_print():
    """argv: ['t.gp']
    t.gp:
        print sum [i=1:3] i, 1
    """
    check("program.iteration_in_print")


def test_error_inside_loop():
    """argv: ['t.gp']
    t.gp:
        do for [i=1:5] {
          print i
          if (i == 3) { print undefined_var }
        }
    """
    check("program.error_inside_loop")


def test_error_inside_load():
    """argv: ['t.gp']
    t.gp:
        print 'before'
        load 'bad.gp'
        print 'after'
    """
    check("program.error_inside_load")


def test_reread_and_pause():
    """argv: ['t.gp']
    t.gp:
        pause 0
        pause 0 'message shown'
        print 'ok'
    """
    check("program.reread_and_pause")


def test_evaluate_with_reset():
    """argv: ['t.gp']
    t.gp:
        set samples 7
        reset
        show samples
    """
    check("program.evaluate_with_reset")
