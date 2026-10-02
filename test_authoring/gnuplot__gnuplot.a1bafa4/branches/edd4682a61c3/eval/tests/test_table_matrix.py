"""Behavioural tests: table_matrix (24 cases, golden outputs in golden/table_matrix.json)."""
from eval.tests._harness import check


def test_poly__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] x**3 - 3*x
    """
    check("table_matrix.poly__s7")


def test_poly__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] x**3 - 3*x
    """
    check("table_matrix.poly__log")


def test_poly__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] x**3 - 3*x
    """
    check("table_matrix.poly__y_restricted")


def test_gauss__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] exp(-x**2)
    """
    check("table_matrix.gauss__s7")


def test_gauss__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] exp(-x**2)
    """
    check("table_matrix.gauss__log")


def test_gauss__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] exp(-x**2)
    """
    check("table_matrix.gauss__y_restricted")


def test_sinc__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] x == 0 ? 1 : sin(3*x)/(3*x)
    """
    check("table_matrix.sinc__s7")


def test_sinc__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] x == 0 ? 1 : sin(3*x)/(3*x)
    """
    check("table_matrix.sinc__log")


def test_sinc__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] x == 0 ? 1 : sin(3*x)/(3*x)
    """
    check("table_matrix.sinc__y_restricted")


def test_abs_saw__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] abs(x - floor(x) - 0.5)
    """
    check("table_matrix.abs_saw__s7")


def test_abs_saw__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] abs(x - floor(x) - 0.5)
    """
    check("table_matrix.abs_saw__log")


def test_abs_saw__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] abs(x - floor(x) - 0.5)
    """
    check("table_matrix.abs_saw__y_restricted")


def test_step__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] x < 0 ? -1 : 1
    """
    check("table_matrix.step__s7")


def test_step__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] x < 0 ? -1 : 1
    """
    check("table_matrix.step__log")


def test_step__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] x < 0 ? -1 : 1
    """
    check("table_matrix.step__y_restricted")


def test_lin__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] 0.5*x + 1
    """
    check("table_matrix.lin__s7")


def test_lin__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] 0.5*x + 1
    """
    check("table_matrix.lin__log")


def test_lin__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] 0.5*x + 1
    """
    check("table_matrix.lin__y_restricted")


def test_atan__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] atan(2*x)
    """
    check("table_matrix.atan__s7")


def test_atan__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] atan(2*x)
    """
    check("table_matrix.atan__log")


def test_atan__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] atan(2*x)
    """
    check("table_matrix.atan__y_restricted")


def test_cosh__s7():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 7
        plot [-2:2] cosh(x)/10
    """
    check("table_matrix.cosh__s7")


def test_cosh__log():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 6
        set logscale x
        plot [0.1:10] cosh(x)/10
    """
    check("table_matrix.cosh__log")


def test_cosh__y_restricted():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        set yrange [-0.5:0.5]
        plot [-2:2] cosh(x)/10
    """
    check("table_matrix.cosh__y_restricted")
