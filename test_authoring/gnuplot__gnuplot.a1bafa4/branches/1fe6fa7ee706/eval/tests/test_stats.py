"""Behavioural tests: stats (13 cases, golden outputs in golden/stats.json)."""
from eval.tests._harness import check


def test_two_columns():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats $d
    """
    check("stats.two_columns")


def test_single_column():
    """argv: ['t.gp']
    t.gp:
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
        stats $s
    """
    check("stats.single_column")


def test_named_prefix_variables():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats $d using 2 name 'Y' nooutput
        print Y_mean, Y_stddev, Y_min, Y_max, Y_median, Y_records, Y_sum, Y_lo_quartile, Y_up_quartile
    """
    check("stats.named_prefix_variables")


def test_default_variables():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats $d nooutput
        print STATS_correlation, STATS_slope, STATS_intercept, STATS_mean_x, STATS_mean_y, STATS_sumxy, STATS_pos_max_y
    """
    check("stats.default_variables")


def test_multiple_blocks():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        # x y err
        0 1.0 0.1
        1 2.7 0.2
        2 7.4 0.3
        3 20.1 0.5
        4 54.6 1.0
        
        
        0 3
        1 2
        2 4
        3 1
        4 5
        EOD
        stats $d
    """
    check("stats.multiple_blocks")


def test_index_and_every():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        # x y err
        0 1.0 0.1
        1 2.7 0.2
        2 7.4 0.3
        3 20.1 0.5
        4 54.6 1.0
        
        
        0 3
        1 2
        2 4
        3 1
        4 5
        EOD
        stats $d index 1 every 2 using 2
    """
    check("stats.index_and_every")


def test_with_missing_and_invalid():
    """argv: ['t.gp']
    t.gp:
        $m << EOD
        1 2
        2 ?
        3 x
        4 8
        
        5 10
        EOD
        set datafile missing '?'
        stats $m
    """
    check("stats.with_missing_and_invalid")


def test_range_restricted():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats [2:5] $d using 1:2
    """
    check("stats.range_restricted")


def test_matrix():
    """argv: ['t.gp']
    t.gp:
        $m << EOD
        1 2 3
        4 5 6
        EOD
        stats $m matrix
    """
    check("stats.matrix")


def test_expression_columns():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats $d using ($1*2):(log($2))
    """
    check("stats.expression_columns")


def test_noisy_data():
    """argv: ['t.gp']
    t.gp:
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
        23 10.5
        ...
    """
    check("stats.noisy_data")


def test_show_variables_after():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        stats $d using 1 nooutput
        show variables STATS_
    """
    check("stats.show_variables_after")


def test_output_to_print_file():
    """argv: ['t.gp']
    t.gp:
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set print 'stats.txt'
        stats $d
        set print
        print 'done'
    """
    check("stats.output_to_print_file")
