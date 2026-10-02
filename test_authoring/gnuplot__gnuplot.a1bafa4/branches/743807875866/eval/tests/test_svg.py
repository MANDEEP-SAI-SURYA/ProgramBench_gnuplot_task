"""Behavioural tests: svg (6 cases, golden outputs in golden/svg.json)."""
from eval.tests._harness import check


def test_basic_lines():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        plot [0:1] x, x**2
    """
    check("svg.basic_lines")


def test_points_and_key():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        $d << EOD
        1 1
        2 3
        3 2
        EOD
        set key left
        plot $d with points pt 7 title 'pts'
    """
    check("svg.points_and_key")


def test_title_labels():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        set title 'T'
        set xlabel 'X axis'
        set ylabel 'Y'
        plot [0:2] sin(x)
    """
    check("svg.title_labels")


def test_boxes_fill():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        $d << EOD
        1 1
        2 3
        3 2
        EOD
        set style fill solid 0.5
        plot $d with boxes
    """
    check("svg.boxes_fill")


def test_logscale_grid():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        set logscale y
        set grid
        plot [1:10] exp(x)
    """
    check("svg.logscale_grid")


def test_dashed_colors():
    """argv: ['t.gp']
    t.gp:
        set term svg size 320,240 font 'Sans,10'
        plot [0:1] x lc rgb 'red' dt 2, x**2 lc rgb '#00ff00' lw 3
    """
    check("svg.dashed_colors")
