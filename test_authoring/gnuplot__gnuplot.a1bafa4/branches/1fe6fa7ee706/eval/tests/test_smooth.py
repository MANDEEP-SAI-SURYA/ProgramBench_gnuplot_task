"""Behavioural tests: smooth (24 cases, golden outputs in golden/smooth.json)."""
from eval.tests._harness import check


def test_unique():
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
    check("smooth.unique")


def test_frequency():
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
    check("smooth.frequency")


def test_fnormal():
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
    check("smooth.fnormal")


def test_cumulative():
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
    check("smooth.cumulative")


def test_cnormal():
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
    check("smooth.cnormal")


def test_csplines():
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
    check("smooth.csplines")


def test_acsplines():
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
    check("smooth.acsplines")


def test_mcsplines():
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
    check("smooth.mcsplines")


def test_bezier():
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
    check("smooth.bezier")


def test_sbezier():
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
    check("smooth.sbezier")


def test_kdensity():
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
    check("smooth.kdensity")


def test_path():
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
    check("smooth.path")


def test_unique_averages_duplicates():
    """argv: ['t.gp']
    t.gp:
        set table
        $u << EOD
        3 1
        1 2
        3 5
        2 2
        1 4
        EOD
        plot $u smooth unique, $u smooth frequency
    """
    check("smooth.unique_averages_duplicates")


def test_kdensity_bandwidth():
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
        set samples 12
        plot $s using 1:(1) smooth kdensity bandwidth 0.7, $s using 1:(1) smooth kdensity
    """
    check("smooth.kdensity_bandwidth")


def test_kdensity_period():
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
        set samples 10
        plot $s using 1:(1) smooth kdensity bandwidth 1.0 period 6
    """
    check("smooth.kdensity_period")


def test_bins():
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
        plot $s using 1:(1) bins=5, $s using 1:(1) bins binwidth=2 binrange [0:14]
    """
    check("smooth.bins")


def test_acsplines_weights():
    """argv: ['t.gp']
    t.gp:
        set table
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set samples 10
        plot $d using 1:2:(1e-3) smooth acsplines, $d using 1:2:(100) smooth acsplines
    """
    check("smooth.acsplines_weights")


def test_csplines_two_points():
    """argv: ['t.gp']
    t.gp:
        set table
        $p << EOD
        0 0
        1 1
        EOD
        set samples 5
        plot $p smooth csplines
    """
    check("smooth.csplines_two_points")


def test_cumulative_normalized():
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
        plot $s using 1:(1) smooth cnormal, $s using 1:(1) smooth cumulative
    """
    check("smooth.cumulative_normalized")


def test_bezier_samples():
    """argv: ['t.gp']
    t.gp:
        set table
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set samples 7
        plot $d smooth bezier, $d smooth sbezier
    """
    check("smooth.bezier_samples")


def test_smooth_with_log():
    """argv: ['t.gp']
    t.gp:
        set table
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set logscale y
        set samples 6
        plot $d smooth csplines
    """
    check("smooth.smooth_with_log")


def test_zsort_and_convexhull():
    """argv: ['t.gp']
    t.gp:
        set table
        $p << EOD
        0 0
        2 0
        1 1
        2 2
        0 2
        1 3
        EOD
        plot $p smooth convexhull, $p using 1:2:(-$2) smooth zsort
    """
    check("smooth.zsort_and_convexhull")


def test_unwrap():
    """argv: ['t.gp']
    t.gp:
        set table
        $p << EOD
        0 3.0
        1 -3.0
        2 3.1
        3 -2.9
        EOD
        plot $p smooth unwrap
    """
    check("smooth.unwrap")


def test_mcsplines_monotone():
    """argv: ['t.gp']
    t.gp:
        set table
        $p << EOD
        0 0
        1 0
        2 1
        3 1
        4 5
        EOD
        set samples 9
        plot $p smooth mcsplines
    """
    check("smooth.mcsplines_monotone")
