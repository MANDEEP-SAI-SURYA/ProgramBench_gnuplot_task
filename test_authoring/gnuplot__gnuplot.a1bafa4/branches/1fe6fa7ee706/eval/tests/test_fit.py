"""Behavioural tests: fit (13 cases, golden outputs in golden/fit.json)."""
from eval.tests._harness import check


def test_linear():
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
        f(x) = a*x + b
        fit f(x) $d via a, b
    """
    check("fit.linear")


def test_quadratic_quiet():
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
        set fit quiet
        f(x) = a*x**2 + b*x + c
        fit f(x) $d via a, b, c
        print a, b, c
        print FIT_NDF, FIT_WSSR, FIT_STDFIT, FIT_CONVERGED
    """
    check("fit.quadratic_quiet")


def test_exponential_with_errors():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        # x y err
        0 1.0 0.1
        1 2.7 0.2
        2 7.4 0.3
        3 20.1 0.5
        4 54.6 1.0
        
        
        0 3
        1 2
        2 4
        3 1
        4 5
        EOD
        set fit logfile 'my.log'
        g(x) = A*exp(k*x)
        A = 1; k = 1
        fit g(x) $d index 0 using 1:2:3 yerrors via A, k
    """
    check("fit.exponential_with_errors")


def test_brief_errorvariables():
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
        set fit brief errorvariables nolog
        fit m*x + q $d via m, q
        print m, m_err, q, q_err
    """
    check("fit.brief_errorvariables")


def test_verbose():
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
        set fit verbose nolog
        fit m*x $d via m
    """
    check("fit.verbose")


def test_limits_and_start():
    """argv: ['t.gp']
    t.gp:
        $n << EOD
        0 -5.0
        1 -0.5
        2 4.0
        3 -2.5
        4 2.0
        5 6.5
        6 0.0
        7 4.5
        8 9.0
        9 2.5
        10 7.0
        11 0.5
        12 5.0
        13 9.5
        14 3.0
        15 7.5
        16 12.0
        17 5.5
        18 10.0
        19 14.5
        20 8.0
        21 12.5
        22 6.0
        23 10.5
        ...
    """
    check("fit.limits_and_start")


def test_maxiter_hit():
    """argv: ['t.gp']
    t.gp:
        $n << EOD
        0 -5.0
        1 -0.5
        2 4.0
        3 -2.5
        4 2.0
        5 6.5
        6 0.0
        7 4.5
        8 9.0
        9 2.5
        10 7.0
        11 0.5
        12 5.0
        13 9.5
        14 3.0
        15 7.5
        16 12.0
        17 5.5
        18 10.0
        19 14.5
        20 8.0
        21 12.5
        22 6.0
        23 10.5
        ...
    """
    check("fit.maxiter_hit")


def test_fit_ranges():
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
        set fit nolog
        fit [2:5] a*x + b $d via a, b
    """
    check("fit.fit_ranges")


def test_fixed_parameter_file():
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
        set fit nolog
        fit a*x + b $d via 'start.par'
        print a, b
    """
    check("fit.fixed_parameter_file")


def test_covariance_variables():
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
        set fit quiet nolog covariancevariables
        fit a*x + b $d via a, b
        print FIT_COV_a_b, FIT_COV_a_a
    """
    check("fit.covariance_variables")


def test_two_dimensional():
    """argv: ['t.gp']
    t.gp:
        $g << EOD
        0 0 1
        0 1 3
        1 0 2
        1 1 4.2
        2 1 5.1
        2 2 7
        EOD
        set fit nolog
        fit a*x + b*y + c $g using 1:2:3:(1) via a, b, c
    """
    check("fit.two_dimensional")


def test_singular_fit():
    """argv: ['t.gp']
    t.gp:
        $z << EOD
        1 1
        1 1
        1 1
        EOD
        set fit nolog
        fit a*x + b $z via a, b
    """
    check("fit.singular_fit")


def test_update_file():
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
        set fit nolog quiet
        a = 1; b = 1
        fit a*x + b $d via a, b
        update 'p.par'
    """
    check("fit.update_file")
