"""Behavioural tests: dumb3d (20 cases, golden outputs in golden/dumb3d.json)."""
from eval.tests._harness import check


def test_saddle__default():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        splot [-2:2][-2:2] x**2 - y**2 title 'saddle'
    """
    check("dumb3d.saddle__default")


def test_saddle__view_60_30():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view 60, 30
        splot [-2:2][-2:2] x**2 - y**2 title 'saddle'
    """
    check("dumb3d.saddle__view_60_30")


def test_saddle__hidden3d():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set hidden3d
        splot [-2:2][-2:2] x**2 - y**2 title 'saddle'
    """
    check("dumb3d.saddle__hidden3d")


def test_saddle__map_contour():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view map
        set contour base
        set cntrparam levels 4
        unset surface
        splot [-2:2][-2:2] x**2 - y**2 title 'saddle'
    """
    check("dumb3d.saddle__map_contour")


def test_saddle__ticslevel0_iso6():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set ticslevel 0
        set isosamples 6
        splot [-2:2][-2:2] x**2 - y**2 title 'saddle'
    """
    check("dumb3d.saddle__ticslevel0_iso6")


def test_bump__default():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        splot [-2:2][-2:2] exp(-(x**2+y**2)) title 'bump'
    """
    check("dumb3d.bump__default")


def test_bump__view_60_30():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view 60, 30
        splot [-2:2][-2:2] exp(-(x**2+y**2)) title 'bump'
    """
    check("dumb3d.bump__view_60_30")


def test_bump__hidden3d():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set hidden3d
        splot [-2:2][-2:2] exp(-(x**2+y**2)) title 'bump'
    """
    check("dumb3d.bump__hidden3d")


def test_bump__map_contour():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view map
        set contour base
        set cntrparam levels 4
        unset surface
        splot [-2:2][-2:2] exp(-(x**2+y**2)) title 'bump'
    """
    check("dumb3d.bump__map_contour")


def test_bump__ticslevel0_iso6():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set ticslevel 0
        set isosamples 6
        splot [-2:2][-2:2] exp(-(x**2+y**2)) title 'bump'
    """
    check("dumb3d.bump__ticslevel0_iso6")


def test_ripple__default():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        splot [-2:2][-2:2] sin(x)*cos(y) title 'ripple'
    """
    check("dumb3d.ripple__default")


def test_ripple__view_60_30():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view 60, 30
        splot [-2:2][-2:2] sin(x)*cos(y) title 'ripple'
    """
    check("dumb3d.ripple__view_60_30")


def test_ripple__hidden3d():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set hidden3d
        splot [-2:2][-2:2] sin(x)*cos(y) title 'ripple'
    """
    check("dumb3d.ripple__hidden3d")


def test_ripple__map_contour():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view map
        set contour base
        set cntrparam levels 4
        unset surface
        splot [-2:2][-2:2] sin(x)*cos(y) title 'ripple'
    """
    check("dumb3d.ripple__map_contour")


def test_ripple__ticslevel0_iso6():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set ticslevel 0
        set isosamples 6
        splot [-2:2][-2:2] sin(x)*cos(y) title 'ripple'
    """
    check("dumb3d.ripple__ticslevel0_iso6")


def test_plane__default():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        splot [-2:2][-2:2] x + 2*y title 'plane'
    """
    check("dumb3d.plane__default")


def test_plane__view_60_30():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view 60, 30
        splot [-2:2][-2:2] x + 2*y title 'plane'
    """
    check("dumb3d.plane__view_60_30")


def test_plane__hidden3d():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set hidden3d
        splot [-2:2][-2:2] x + 2*y title 'plane'
    """
    check("dumb3d.plane__hidden3d")


def test_plane__map_contour():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set view map
        set contour base
        set cntrparam levels 4
        unset surface
        splot [-2:2][-2:2] x + 2*y title 'plane'
    """
    check("dumb3d.plane__map_contour")


def test_plane__ticslevel0_iso6():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        set ticslevel 0
        set isosamples 6
        splot [-2:2][-2:2] x + 2*y title 'plane'
    """
    check("dumb3d.plane__ticslevel0_iso6")
