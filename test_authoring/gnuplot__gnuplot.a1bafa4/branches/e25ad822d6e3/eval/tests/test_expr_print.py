"""Behavioural tests: expr_print (15 cases, golden outputs in golden/expr_print.json)."""
from eval.tests._harness import check


def test_e00():
    """argv: ['t.gp']
    t.gp:
        print 1/7.0
        print sprintf('%.17g', 1/7.0)
    """
    check("expr_print.e00")


def test_e02():
    """argv: ['t.gp']
    t.gp:
        print 10**15/3.0
        print sprintf('%.17g', 10**15/3.0)
    """
    check("expr_print.e02")


def test_e04():
    """argv: ['t.gp']
    t.gp:
        print -0.0
        print sprintf('%.17g', -0.0)
    """
    check("expr_print.e04")


def test_e06():
    """argv: ['t.gp']
    t.gp:
        print 123456789012
        print sprintf('%.17g', 123456789012)
    """
    check("expr_print.e06")


def test_e08():
    """argv: ['t.gp']
    t.gp:
        print 2.0**53+1
        print sprintf('%.17g', 2.0**53+1)
    """
    check("expr_print.e08")


def test_e10():
    """argv: ['t.gp']
    t.gp:
        print 7.0/3*3
        print sprintf('%.17g', 7.0/3*3)
    """
    check("expr_print.e10")


def test_e12():
    """argv: ['t.gp']
    t.gp:
        print exp(-10)
        print sprintf('%.17g', exp(-10))
    """
    check("expr_print.e12")


def test_e14():
    """argv: ['t.gp']
    t.gp:
        print pi*1e-3
        print sprintf('%.17g', pi*1e-3)
    """
    check("expr_print.e14")


def test_e16():
    """argv: ['t.gp']
    t.gp:
        print sqrt(1e-30)
        print sprintf('%.17g', sqrt(1e-30))
    """
    check("expr_print.e16")


def test_e18():
    """argv: ['t.gp']
    t.gp:
        print 1e16/3
        print sprintf('%.17g', 1e16/3)
    """
    check("expr_print.e18")


def test_e20():
    """argv: ['t.gp']
    t.gp:
        print 0.1*3
        print sprintf('%.17g', 0.1*3)
    """
    check("expr_print.e20")


def test_e22():
    """argv: ['t.gp']
    t.gp:
        print -13 % 4
        print sprintf('%.17g', -13 % 4)
    """
    check("expr_print.e22")


def test_e24():
    """argv: ['t.gp']
    t.gp:
        print 13 / -4
        print sprintf('%.17g', 13 / -4)
    """
    check("expr_print.e24")


def test_e26():
    """argv: ['t.gp']
    t.gp:
        print 2**63-1
        print sprintf('%.17g', 2**63-1)
    """
    check("expr_print.e26")


def test_e28():
    """argv: ['t.gp']
    t.gp:
        print 5 ** -1
        print sprintf('%.17g', 5 ** -1)
    """
    check("expr_print.e28")
