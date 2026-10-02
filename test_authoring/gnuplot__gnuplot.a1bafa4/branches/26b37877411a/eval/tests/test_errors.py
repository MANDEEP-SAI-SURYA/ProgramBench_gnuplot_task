"""Behavioural tests: errors (39 cases, golden outputs in golden/errors.json)."""
from eval.tests._harness import check


def test_invalid_expression():
    """argv: ['t.gp']
    t.gp:
        print 1 +
    """
    check("errors.invalid_expression")


def test_unbalanced_paren():
    """argv: ['t.gp']
    t.gp:
        print (1 + 2
    """
    check("errors.unbalanced_paren")


def test_undefined_function():
    """argv: ['t.gp']
    t.gp:
        print nosuch(1)
    """
    check("errors.undefined_function")


def test_wrong_arg_count():
    """argv: ['t.gp']
    t.gp:
        f(x) = x
        print f(1, 2)
    """
    check("errors.wrong_arg_count")


def test_builtin_wrong_args():
    """argv: ['t.gp']
    t.gp:
        print sin(1, 2)
    """
    check("errors.builtin_wrong_args")


def test_string_arith():
    """argv: ['t.gp']
    t.gp:
        print "abc" * 2
    """
    check("errors.string_arith")


def test_unknown_command():
    """argv: ['t.gp']
    t.gp:
        frobnicate the plot
    """
    check("errors.unknown_command")


def test_unknown_set_option():
    """argv: ['t.gp']
    t.gp:
        set nosuchoption
    """
    check("errors.unknown_set_option")


def test_bad_range():
    """argv: ['t.gp']
    t.gp:
        set xrange [5:
    """
    check("errors.bad_range")


def test_bad_range_2():
    """argv: ['t.gp']
    t.gp:
        set xrange [a:b]
    """
    check("errors.bad_range_2")


def test_plot_nothing():
    """argv: ['t.gp']
    t.gp:
        plot
    """
    check("errors.plot_nothing")


def test_plot_undefined_function():
    """argv: ['t.gp']
    t.gp:
        set table
        plot zzz(x)
    """
    check("errors.plot_undefined_function")


def test_plot_missing_datablock():
    """argv: ['t.gp']
    t.gp:
        set table
        plot $nothere
    """
    check("errors.plot_missing_datablock")


def test_plot_missing_file():
    """argv: ['t.gp']
    t.gp:
        set table
        plot 'nonexistent.dat'
    """
    check("errors.plot_missing_file")


def test_bad_using():
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
        set table
        plot $d using 1:(
    """
    check("errors.bad_using")


def test_column_out_of_range():
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
        set table
        plot $d using 1:5
    """
    check("errors.column_out_of_range")


def test_empty_range():
    """argv: ['t.gp']
    t.gp:
        set table
        set xrange [1:1]
        plot x
    """
    check("errors.empty_range")


def test_log_negative_range():
    """argv: ['t.gp']
    t.gp:
        set table
        set logscale y
        set yrange [-1:10]
        plot x
    """
    check("errors.log_negative_range")


def test_set_terminal_unknown():
    """argv: ['t.gp']
    t.gp:
        set terminal nosuchterm
    """
    check("errors.set_terminal_unknown")


def test_set_samples_invalid():
    """argv: ['t.gp']
    t.gp:
        set samples 1
    """
    check("errors.set_samples_invalid")


def test_fit_no_params():
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
        fit a*x $d
    """
    check("errors.fit_no_params")


def test_fit_undefined_function():
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
        fit q(x) $d via a
    """
    check("errors.fit_undefined_function")


def test_do_for_bad():
    """argv: ['t.gp']
    t.gp:
        do for [i=1:] { print i }
    """
    check("errors.do_for_bad")


def test_error_line_numbers():
    """argv: ['t.gp']
    t.gp:
        
        
        x = 1
        
        print x +* 2
        
    """
    check("errors.error_line_numbers")


def test_error_with_long_line():
    """argv: ['t.gp']
    t.gp:
        print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 27
    """
    check("errors.error_with_long_line")


def test_missing_quote():
    """argv: ['t.gp']
    t.gp:
        print "unterminated
    """
    check("errors.missing_quote")


def test_array_bad_index():
    """argv: ['t.gp']
    t.gp:
        array A[3]
        A[0] = 1
    """
    check("errors.array_bad_index")


def test_array_not_array():
    """argv: ['t.gp']
    t.gp:
        x = 1
        print x[1]
    """
    check("errors.array_not_array")


def test_stats_no_data():
    """argv: ['t.gp']
    t.gp:
        stats $nope
    """
    check("errors.stats_no_data")


def test_bad_format_in_gprintf():
    """argv: ['t.gp']
    t.gp:
        print gprintf("%d %d", 1)
    """
    check("errors.bad_format_in_gprintf")


def test_unset_unknown():
    """argv: ['t.gp']
    t.gp:
        unset bogus
    """
    check("errors.unset_unknown")


def test_show_unknown():
    """argv: ['t.gp']
    t.gp:
        show nothinghere
    """
    check("errors.show_unknown")


def test_undefined_in_function_body():
    """argv: ['t.gp']
    t.gp:
        f(x) = x + undefined_y
        print f(1)
    """
    check("errors.undefined_in_function_body")


def test_type_error_bitwise():
    """argv: ['t.gp']
    t.gp:
        print 1.5 & 3
    """
    check("errors.type_error_bitwise")


def test_type_error_modulo_float():
    """argv: ['t.gp']
    t.gp:
        print 5.5 % 2
    """
    check("errors.type_error_modulo_float")


def test_string_index_error():
    """argv: ['t.gp']
    t.gp:
        print "abc"[0:1]
    """
    check("errors.string_index_error")


def test_warning_continues():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set logscale x
        set xrange [-1:10]
        print 'still running'
    """
    check("errors.warning_continues")


def test_error_from_e_flag():
    """argv: ['-e', 'set xrange [1:', '-e', 'print 2']
    """
    check("errors.error_from_e_flag")


def test_error_from_stdin_line():
    """argv: []
    stdin: 'print 1\\n\\nprint 2 +\\nprint 3\\n'
    """
    check("errors.error_from_stdin_line")
