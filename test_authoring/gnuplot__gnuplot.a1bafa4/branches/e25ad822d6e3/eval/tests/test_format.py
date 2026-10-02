"""Behavioural tests: format (14 cases, golden outputs in golden/format.json)."""
from eval.tests._harness import check


def test_sprintf_ints():
    """argv: ['t.gp']
    t.gp:
        print sprintf("[%d] [%5d] [%-5d] [%05d] [%+d] [%x] [%X] [%o] [%#x]", 42, 42, 42, 42, 42, 255, 255, 8, 255)
    """
    check("format.sprintf_ints")


def test_sprintf_floats():
    """argv: ['t.gp']
    t.gp:
        print sprintf("[%f] [%.2f] [%10.3f] [%-10.1f] [%e] [%.3E] [%g] [%G] [%.3g]", pi, pi, pi, pi, 12345.678, 0.000123, 1e-5, 1e20, 1234.5)
    """
    check("format.sprintf_floats")


def test_sprintf_strings():
    """argv: ['t.gp']
    t.gp:
        print sprintf("[%s] [%10s] [%-10s] [%.2s] [%%]", "abc", "abc", "abc", "abc")
    """
    check("format.sprintf_strings")


def test_sprintf_type_coercion():
    """argv: ['t.gp']
    t.gp:
        print sprintf("%d %f %s", 3.9, 2, 7)
        print sprintf("%d", "12")
    """
    check("format.sprintf_type_coercion")


def test_sprintf_errors_too_few():
    """argv: ['t.gp']
    t.gp:
        print sprintf("%d %d", 1)
    """
    check("format.sprintf_errors_too_few")


def test_sprintf_errors_bad():
    """argv: ['t.gp']
    t.gp:
        print sprintf("%s", 1)
    """
    check("format.sprintf_errors_bad")


def test_sprintf_many():
    """argv: ['t.gp']
    t.gp:
        print sprintf("%s=%d;%s=%.1f", "a", 1, "b", 2.25)
    """
    check("format.sprintf_many")


def test_gprintf_basic():
    """argv: ['t.gp']
    t.gp:
        print gprintf("%g", 1234.5), gprintf("%.3f", 2), gprintf("%t", 1234.5), gprintf("%T", 1234.5), gprintf("%l", 1234.5), gprintf("%L", 1234.5)
    """
    check("format.gprintf_basic")


def test_gprintf_mantissa_exponent():
    """argv: ['t.gp']
    t.gp:
        do for [v in "0.000123 1 999 1e6 2.5e-9 -42"] { print gprintf("%.2t x 10^%T", v+0), gprintf("%s%c", v+0), gprintf("%.1s %c", v+0) }
    """
    check("format.gprintf_mantissa_exponent")


def test_gprintf_pi_and_binary():
    """argv: ['t.gp']
    t.gp:
        print gprintf("%P", pi), gprintf("%.2P", 2.5*pi), gprintf("%b", 4096), gprintf("%B", 4096), gprintf("%h", 1e-5)
    """
    check("format.gprintf_pi_and_binary")


def test_gprintf_combined():
    """argv: ['t.gp']
    t.gp:
        print gprintf("value: %5.2f units", 3.14159), gprintf("%x", 255), gprintf("%o", 8)
    """
    check("format.gprintf_combined")


def test_print_default_format():
    """argv: ['t.gp']
    t.gp:
        print 1.0, 0.1, 1e6, 1e16, 1e17, 123456.7, 1234567.8, 0.00012345, 3.0e-7
    """
    check("format.print_default_format")


def test_format_command_and_show():
    """argv: ['t.gp']
    t.gp:
        set format x "%.2f"
        set format y "%g units"
        set format z "%t"
        show format
    """
    check("format.format_command_and_show")


def test_set_decimalsign():
    """argv: ['t.gp']
    t.gp:
        set decimalsign ","
        print gprintf("%.3f", pi)
        print sprintf("%.3f", pi)
    """
    check("format.set_decimalsign")
