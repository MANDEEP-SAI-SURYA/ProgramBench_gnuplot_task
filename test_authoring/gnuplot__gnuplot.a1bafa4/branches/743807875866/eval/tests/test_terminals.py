"""Behavioural tests: terminals (7 cases, golden outputs in golden/terminals.json)."""
from eval.tests._harness import check


def test_svg_simple():
    """argv: ['t.gp']
    t.gp:
        set term svg size 300,200
        plot [0:1] x
    """
    check("terminals.svg_simple")


def test_svg_with_text():
    """argv: ['t.gp']
    t.gp:
        set term svg size 200,150 font 'Arial,10'
        set title 'Hello & <World>'
        plot [0:1] x**2 title 'quad'
    """
    check("terminals.svg_with_text")


def test_canvas_simple():
    """argv: ['t.gp']
    t.gp:
        set term canvas size 200,100
        plot [0:1] x
    """
    check("terminals.canvas_simple")


def test_postscript_header_tail():
    """argv: ['t.gp']
    t.gp:
        set term postscript eps
        set output 'p.eps'
        plot [0:1] x
        set output
        print 'done'
    """
    check("terminals.postscript_header_tail")


def test_show_terminal_dumb():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,20 ansi
        show terminal
    """
    check("terminals.show_terminal_dumb")


def test_unknown_terminal_option():
    """argv: ['t.gp']
    t.gp:
        set term dumb bogus
    """
    check("terminals.unknown_terminal_option")


def test_term_list():
    """argv: ['t.gp']
    t.gp:
        set term dumb
        show term
        set term push
        set term svg
        set term pop
        show term
    """
    check("terminals.term_list")
