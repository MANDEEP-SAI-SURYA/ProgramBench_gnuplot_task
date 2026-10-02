"""Behavioural tests: multiplot (6 cases, golden outputs in golden/multiplot.json)."""
from eval.tests._harness import check


def test_layout_0():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 90,30
        set multiplot layout 2,1
        plot [-2:2] sin(x)
        plot [-2:2] cos(x)
        unset multiplot
    """
    check("multiplot.layout_0")


def test_layout_1():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 90,30
        set multiplot layout 2,2
        plot [-2:2] x
        plot [-2:2] x**2
        plot [-2:2] -x
        plot [-2:2] abs(x)
        unset multiplot
    """
    check("multiplot.layout_1")


def test_layout_2():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 90,30
        set multiplot layout 1,3 title 'three'
        plot [-2:2] 1
        plot [-2:2] x
        plot [-2:2] x**3
        unset multiplot
    """
    check("multiplot.layout_2")


def test_layout_3():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 90,30
        set multiplot layout 2,2 rowsfirst downwards
        plot [-2:2] x
        plot [-2:2] 2*x
        plot [-2:2] 3*x
        unset multiplot
    """
    check("multiplot.layout_3")


def test_layout_4():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 90,30
        set multiplot layout 2,1 margins 0.1,0.9,0.1,0.9 spacing 0.05
        plot [-2:2] exp(x)
        plot [-2:2] log(abs(x)+1)
        unset multiplot
    """
    check("multiplot.layout_4")


def test_manual_size_origin():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 80,30
        set multiplot
        set size 0.5,0.5
        set origin 0,0
        plot [0:1] x
        set origin 0.5,0.5
        plot [0:1] 1-x
        unset multiplot
    """
    check("multiplot.manual_size_origin")
