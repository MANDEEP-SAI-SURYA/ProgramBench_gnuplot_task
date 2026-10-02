"""Behavioural tests: expr (36 cases, golden outputs in golden/expr.json)."""
from eval.tests._harness import check


def test_int_arith():
    """argv: ['t.gp']
    t.gp:
        print 7/2, -7/2, 7%3, -7%3, 7.0/2, 2**10, 2**-1, 2.0**-1, -2**2, (-2)**2
    """
    check("expr.int_arith")


def test_int_overflow():
    """argv: ['t.gp']
    t.gp:
        print 2**62, 2**63, 2**64, 9223372036854775807 + 1, -9223372036854775807 - 2, 3037000500**2
    """
    check("expr.int_overflow")


def test_float_print_precision():
    """argv: ['t.gp']
    t.gp:
        print 1/3.0, 2/3.0, 1e20, 1e-20, 123456789.123456789, 0.1+0.2, 1e15+0.3, 100.0, 1e300*1e10, -1e300*1e10
    """
    check("expr.float_print_precision")


def test_nan_inf():
    """argv: ['t.gp']
    t.gp:
        x = 1e308*10
        print x, -x, x-x, (x-x)==(x-x), x>1e308, sqrt(-1), log(0), log(-1)
    """
    check("expr.nan_inf")


def test_division_by_zero():
    """argv: ['t.gp']
    t.gp:
        print 1/0
        print 1.0/0
        print 1%0
    """
    check("expr.division_by_zero")


def test_bit_ops():
    """argv: ['t.gp']
    t.gp:
        print 12 & 10, 12 | 10, 12 ^ 10, ~5, 1 << 4, 256 >> 3, -16 >> 2
    """
    check("expr.bit_ops")


def test_logic_and_compare():
    """argv: ['t.gp']
    t.gp:
        print 1 && 0, 1 || 0, !0, !5, 3 > 2, 3 < 2, 2 >= 2, 2 <= 1, 1 == 1.0, 1 != 2, "a" eq "a", "a" ne "b"
    """
    check("expr.logic_and_compare")


def test_ternary_and_comma():
    """argv: ['t.gp']
    t.gp:
        x = 5
        print x > 3 ? "big" : "small", (a=1, b=2, a+b), x < 3 ? 1 : x < 10 ? 2 : 3
    """
    check("expr.ternary_and_comma")


def test_complex_numbers():
    """argv: ['t.gp']
    t.gp:
        z = {3,4}
        print z, abs(z), real(z), imag(z), arg(z), z*z, z/{0,1}, sqrt({-4,0}), exp({0,pi}), {1,1}**2
    """
    check("expr.complex_numbers")


def test_string_ops():
    """argv: ['t.gp']
    t.gp:
        s = "Hello, World"
        print s[1:5], s[8:], s[:3], strlen(s), strstrt(s, "World"), s . "!", substr(s, 3, 4), upper(s), lower(s)
    """
    check("expr.string_ops")


def test_string_number_coercion():
    """argv: ['t.gp']
    t.gp:
        print "3" + 4, "2.5" * 2, 5 . "", "10" == 10, "abc" + 1
    """
    check("expr.string_number_coercion")


def test_words_and_trim():
    """argv: ['t.gp']
    t.gp:
        s = "  alpha beta	gamma  "
        print words(s), word(s, 2), word(s, 4), "[" . trim(s) . "]"
    """
    check("expr.words_and_trim")


def test_string_functions_more():
    """argv: ['t.gp']
    t.gp:
        print strstrt("abc", "z"), sprintf("%s-%s", "a", "b"), gprintf("%.2f", pi), strlen(""), "x"[1:0]
    """
    check("expr.string_functions_more")


def test_math_functions():
    """argv: ['t.gp']
    t.gp:
        print sin(1), cos(1), tan(1), asin(0.5), acos(0.5), atan(1), atan2(1,-1), sinh(1), cosh(1), tanh(1)
    """
    check("expr.math_functions")


def test_math_functions_2():
    """argv: ['t.gp']
    t.gp:
        print exp(1), log(10), log10(1000), sqrt(2), abs(-3), abs(-3.5), sgn(-2), sgn(0), sgn(4.2)
    """
    check("expr.math_functions_2")


def test_rounding():
    """argv: ['t.gp']
    t.gp:
        print int(3.7), int(-3.7), floor(-3.5), ceil(-3.5), floor(3), round(2.5), round(-2.5), round(3.49)
    """
    check("expr.rounding")


def test_special_functions():
    """argv: ['t.gp']
    t.gp:
        print gamma(5), lgamma(10), erf(0.5), erfc(0.5), inverf(0.5), norm(1), invnorm(0.975), besj0(1), besj1(1), besy0(1), besy1(1)
    """
    check("expr.special_functions")


def test_special_functions_2():
    """argv: ['t.gp']
    t.gp:
        print igamma(2, 1), ibeta(2, 3, 0.4), lambertw(1), airy(1), expint(1, 1), voigt(1, 1)
    """
    check("expr.special_functions_2")


def test_degrees_mode():
    """argv: ['t.gp']
    t.gp:
        set angles degrees
        print sin(30), cos(60), atan(1), asin(1), atan2(1, 1)
        set angles radians
        print sin(30)
    """
    check("expr.degrees_mode")


def test_user_functions():
    """argv: ['t.gp']
    t.gp:
        f(x) = x**2 + 1
        g(x, y) = f(x) * y
        fact(n) = n <= 1 ? 1 : n * fact(n - 1)
        print f(3), g(2, 3), fact(10), fact(20), fact(21)
    """
    check("expr.user_functions")


def test_function_recursion_depth():
    """argv: ['t.gp']
    t.gp:
        r(n) = n == 0 ? 0 : 1 + r(n-1)
        print r(100)
        print r(300000)
    """
    check("expr.function_recursion_depth")


def test_variables_and_exists():
    """argv: ['t.gp']
    t.gp:
        a = 1
        print exists("a"), exists("zz")
        undefine a
        print exists("a")
    """
    check("expr.variables_and_exists")


def test_sum_operator():
    """argv: ['t.gp']
    t.gp:
        print sum [i=1:10] i, sum [i=1:4] i**2, sum [k=5:1] k, sum [i=1:3] 1.0/i
    """
    check("expr.sum_operator")


def test_arrays():
    """argv: ['t.gp']
    t.gp:
        array A[4]
        A[1] = 10; A[2] = "two"; A[4] = {1,1}
        print A
        print |A|, A[2], A[1] + 1
        array B = [3, 1, 2]
        print B, B[3]
    """
    check("expr.arrays")


def test_array_errors():
    """argv: ['t.gp']
    t.gp:
        array A[2]
        print A[3]
    """
    check("expr.array_errors")


def test_integer_valued_functions():
    """argv: ['t.gp']
    t.gp:
        print int(1e18), int(1e19), int(-0.5), floor(1e10), 7.9 % 2, 2**0, 0**0
    """
    check("expr.integer_valued_functions")


def test_rand_reproducible():
    """argv: ['t.gp']
    t.gp:
        print rand(0)
        print rand(0), rand(0)
        print rand(42)
        print rand(0)
    """
    check("expr.rand_reproducible")


def test_time_functions():
    """argv: ['t.gp']
    t.gp:
        print strftime("%Y-%m-%d %H:%M:%S", 0), strftime("%j %a %b", 86400*45.5), strptime("%Y-%m-%d", "2021-03-04"), time_tm = 1000000000
    """
    check("expr.time_functions")


def test_time_functions_2():
    """argv: ['t.gp']
    t.gp:
        t = strptime("%d/%m/%Y %H:%M", "25/12/2020 18:30")
        print t, strftime("%A %B %d %y %I%p", t), tm_year(t), tm_mon(t), tm_mday(t), tm_wday(t), tm_yday(t), tm_hour(t)
    """
    check("expr.time_functions_2")


def test_column_outside_plot():
    """argv: ['t.gp']
    t.gp:
        print column(1)
    """
    check("expr.column_outside_plot")


def test_valid_and_value():
    """argv: ['t.gp']
    t.gp:
        x = 3
        print value("x"), value("x") * 2
    """
    check("expr.valid_and_value")


def test_print_many_types():
    """argv: ['t.gp']
    t.gp:
        print 1, 1.0, "s", {1,0}, {0,-1.5}, 1e-5, 12345678901234
    """
    check("expr.print_many_types")


def test_precedence():
    """argv: ['t.gp']
    t.gp:
        print 2 + 3 * 4 ** 2, -3 ** 2, 2 ** 3 ** 2, 10 - 2 - 3, 100 / 10 / 5, 1 < 2 == 1, !1 + 1
    """
    check("expr.precedence")


def test_string_compare_numbers():
    """argv: ['t.gp']
    t.gp:
        print "10" < "9", 10 < 9, "abc" eq "ab" . "c"
    """
    check("expr.string_compare_numbers")


def test_factorial_operator():
    """argv: ['t.gp']
    t.gp:
        print 5!, 0!, 20!, 3!!
    """
    check("expr.factorial_operator")


def test_hex_octal_literals():
    """argv: ['t.gp']
    t.gp:
        print 0x1F, 0X10, 017, 0b101, 1.5e3, .5, 5.
    """
    check("expr.hex_octal_literals")
