"""Behavioural tests: table3d (12 cases, golden outputs in golden/table3d.json)."""
from eval.tests._harness import check


def test_saddle__grid():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 4, 3
        splot [-1:1][-1:1] x**2 - y**2
    """
    check("table3d.saddle__grid")


def test_saddle__contour():
    """argv: ['t.gp']
    t.gp:
        set table
        set contour base
        set cntrparam levels 3
        unset surface
        set isosamples 8
        splot [-2:2][-2:2] x**2 - y**2
    """
    check("table3d.saddle__contour")


def test_saddle__dgrid3d():
    """argv: ['t.gp']
    t.gp:
        set table
        $p << EOD
        0 0 1
        1 0 2
        0 1 3
        1 1 1
        0.5 0.5 5
        EOD
        set dgrid3d 4,4
        splot $p
    """
    check("table3d.saddle__dgrid3d")


def test_bump__grid():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 4, 3
        splot [-1:1][-1:1] exp(-(x**2+y**2))
    """
    check("table3d.bump__grid")


def test_bump__contour():
    """argv: ['t.gp']
    t.gp:
        set table
        set contour base
        set cntrparam levels 3
        unset surface
        set isosamples 8
        splot [-2:2][-2:2] exp(-(x**2+y**2))
    """
    check("table3d.bump__contour")


def test_bump__dgrid3d():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 3
        set samples 3
        splot [0:2][0:2] exp(-(x**2+y**2)) with points
    """
    check("table3d.bump__dgrid3d")


def test_ripple__grid():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 4, 3
        splot [-1:1][-1:1] sin(x)*cos(y)
    """
    check("table3d.ripple__grid")


def test_ripple__contour():
    """argv: ['t.gp']
    t.gp:
        set table
        set contour base
        set cntrparam levels 3
        unset surface
        set isosamples 8
        splot [-2:2][-2:2] sin(x)*cos(y)
    """
    check("table3d.ripple__contour")


def test_ripple__dgrid3d():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 3
        set samples 3
        splot [0:2][0:2] sin(x)*cos(y) with points
    """
    check("table3d.ripple__dgrid3d")


def test_plane__grid():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 4, 3
        splot [-1:1][-1:1] x + 2*y
    """
    check("table3d.plane__grid")


def test_plane__contour():
    """argv: ['t.gp']
    t.gp:
        set table
        set contour base
        set cntrparam levels 3
        unset surface
        set isosamples 8
        splot [-2:2][-2:2] x + 2*y
    """
    check("table3d.plane__contour")


def test_plane__dgrid3d():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 3
        set samples 3
        splot [0:2][0:2] x + 2*y with points
    """
    check("table3d.plane__dgrid3d")
