"""Behavioural tests: fit_matrix (12 cases, golden outputs in golden/fit_matrix.json)."""
from eval.tests._harness import check


def test_model0():
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
        set fit nolog
        fit a*x + b $d via a,b
    """
    check("fit_matrix.model0")


def test_model0_noisy():
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
    check("fit_matrix.model0_noisy")


def test_model1():
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
        set fit nolog
        a=1; b=0.3
        fit a*exp(b*x) $d via a,b
    """
    check("fit_matrix.model1")


def test_model1_noisy():
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
    check("fit_matrix.model1_noisy")


def test_model2():
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
        set fit nolog
        fit a*x**2 + b*x + c $d via a,b,c
    """
    check("fit_matrix.model2")


def test_model2_noisy():
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
    check("fit_matrix.model2_noisy")


def test_model3():
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
        set fit nolog
        a=12; b=1; c=3
        fit a/(1+exp(-b*(x-c))) $d via a,b,c
    """
    check("fit_matrix.model3")


def test_model3_noisy():
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
    check("fit_matrix.model3_noisy")


def test_model4():
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
        set fit nolog
        fit a*log(x) + b $d via a,b
    """
    check("fit_matrix.model4")


def test_model4_noisy():
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
    check("fit_matrix.model4_noisy")


def test_model5():
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
        set fit nolog
        a=1; b=1; c=2
        fit a*sin(b*x) + c*x $d via a,b,c
    """
    check("fit_matrix.model5")


def test_model5_noisy():
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
    check("fit_matrix.model5_noisy")
