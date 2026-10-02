"""Behavioural tests: smooth_matrix (22 cases, golden outputs in golden/smooth_matrix.json)."""
from eval.tests._harness import check


def test_csplines_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.csplines_sample")


def test_csplines_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.csplines_xrange")


def test_acsplines_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.acsplines_sample")


def test_acsplines_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.acsplines_xrange")


def test_mcsplines_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.mcsplines_sample")


def test_mcsplines_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.mcsplines_xrange")


def test_bezier_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.bezier_sample")


def test_bezier_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.bezier_xrange")


def test_sbezier_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.sbezier_sample")


def test_sbezier_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.sbezier_xrange")


def test_kdensity_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.kdensity_sample")


def test_kdensity_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.kdensity_xrange")


def test_cumulative_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.cumulative_sample")


def test_cumulative_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.cumulative_xrange")


def test_cnormal_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.cnormal_sample")


def test_cnormal_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.cnormal_xrange")


def test_unique_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.unique_sample")


def test_unique_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.unique_xrange")


def test_frequency_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.frequency_sample")


def test_frequency_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.frequency_xrange")


def test_fnormal_sample():
    """argv: ['t.gp']
    t.gp:
        set table
        $s << EOD
        2.1
        3.5
        3.5
        4.0
        4.2
        5.9
        6.1
        6.1
        6.1
        7.4
        8.8
        9.0
        12.5
        3.3
        4.8
        EOD
        $q << EOD
        0 2.1
        1 3.5
        2 3.5
        3 4.0
        4 4.2
        5 5.9
        ...
    """
    check("smooth_matrix.fnormal_sample")


def test_fnormal_xrange():
    """argv: ['t.gp']
    t.gp:
        set table
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
        ...
    """
    check("smooth_matrix.fnormal_xrange")
