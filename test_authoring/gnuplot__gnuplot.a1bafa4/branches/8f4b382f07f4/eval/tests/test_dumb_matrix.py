"""Behavioural tests: dumb_matrix (56 cases, golden outputs in golden/dumb_matrix.json)."""
from eval.tests._harness import check


def test_poly__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__plain")


def test_poly__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__narrow")


def test_poly__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__tall")


def test_poly__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__samples20_points")


def test_poly__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__noborder_keyleft")


def test_poly__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__yrange_grid")


def test_poly__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot x**3 - 3*x title 'poly'
    """
    check("dumb_matrix.poly__impulses_s15")


def test_gauss__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__plain")


def test_gauss__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__narrow")


def test_gauss__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__tall")


def test_gauss__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__samples20_points")


def test_gauss__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__noborder_keyleft")


def test_gauss__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__yrange_grid")


def test_gauss__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot exp(-x**2) title 'gauss'
    """
    check("dumb_matrix.gauss__impulses_s15")


def test_sinc__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__plain")


def test_sinc__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__narrow")


def test_sinc__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__tall")


def test_sinc__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__samples20_points")


def test_sinc__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__noborder_keyleft")


def test_sinc__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__yrange_grid")


def test_sinc__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot x == 0 ? 1 : sin(3*x)/(3*x) title 'sinc'
    """
    check("dumb_matrix.sinc__impulses_s15")


def test_abs_saw__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__plain")


def test_abs_saw__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__narrow")


def test_abs_saw__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__tall")


def test_abs_saw__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__samples20_points")


def test_abs_saw__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__noborder_keyleft")


def test_abs_saw__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__yrange_grid")


def test_abs_saw__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot abs(x - floor(x) - 0.5) title 'abs_saw'
    """
    check("dumb_matrix.abs_saw__impulses_s15")


def test_step__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__plain")


def test_step__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__narrow")


def test_step__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__tall")


def test_step__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__samples20_points")


def test_step__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__noborder_keyleft")


def test_step__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__yrange_grid")


def test_step__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot x < 0 ? -1 : 1 title 'step'
    """
    check("dumb_matrix.step__impulses_s15")


def test_lin__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__plain")


def test_lin__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__narrow")


def test_lin__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__tall")


def test_lin__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__samples20_points")


def test_lin__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__noborder_keyleft")


def test_lin__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__yrange_grid")


def test_lin__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot 0.5*x + 1 title 'lin'
    """
    check("dumb_matrix.lin__impulses_s15")


def test_atan__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__plain")


def test_atan__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__narrow")


def test_atan__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__tall")


def test_atan__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__samples20_points")


def test_atan__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__noborder_keyleft")


def test_atan__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__yrange_grid")


def test_atan__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot atan(2*x) title 'atan'
    """
    check("dumb_matrix.atan__impulses_s15")


def test_cosh__plain():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__plain")


def test_cosh__narrow():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 45,16
        set xrange [-2:2]
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__narrow")


def test_cosh__tall():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,40
        set xrange [-2:2]
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__tall")


def test_cosh__samples20_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 20
        set style function points
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__samples20_points")


def test_cosh__noborder_keyleft():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 70,22
        set xrange [-3:1]
        unset border
        set key left top
        set xtics axis
        set ytics axis
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__noborder_keyleft")


def test_cosh__yrange_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set yrange [-1.5:1.5]
        set grid
        set tics out
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__yrange_grid")


def test_cosh__impulses_s15():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xrange [-2:2]
        set samples 15
        set style function impulses
        plot cosh(x)/10 title 'cosh'
    """
    check("dumb_matrix.cosh__impulses_s15")
