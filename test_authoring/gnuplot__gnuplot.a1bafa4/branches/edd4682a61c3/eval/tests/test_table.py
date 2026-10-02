"""Behavioural tests: table (35 cases, golden outputs in golden/table.json)."""
from eval.tests._harness import check


def test_function_default_samples():
    """argv: ['t.gp']
    t.gp:
        set table
        plot sin(x)
    """
    check("table.function_default_samples")


def test_function_samples_range():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 11
        set xrange [0:1]
        plot x**2, 1-x
    """
    check("table.function_samples_range")


def test_two_functions_titles():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 5
        plot [0:4] x title 'line', x**2 notitle
    """
    check("table.two_functions_titles")


def test_undefined_points():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 9
        plot [-2:2] sqrt(x), 1/x
    """
    check("table.undefined_points")


def test_log_x_sampling():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 8
        set logscale x
        plot [1:1000] log10(x)
    """
    check("table.log_x_sampling")


def test_data_basic():
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
        plot $d
    """
    check("table.data_basic")


def test_data_using_expressions():
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
        plot $d using 1:($2*2), '' using ($1+0.5):(sqrt($2)) title 'sqrt'
    """
    check("table.data_using_expressions")


def test_data_using_column_functions():
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
        plot $d using 0:2, $d using (column(0)):(valid(2) ? $2 : 1/0), $d using 1:(stringcolumn(1).'x')
    """
    check("table.data_using_column_functions")


def test_data_every():
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
        plot $d every 2, $d every ::2::4
    """
    check("table.data_every")


def test_data_index_blocks():
    """argv: ['t.gp']
    t.gp:
        set table
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
        plot $d index 0 using 1:2, $d index 1
    """
    check("table.data_index_blocks")


def test_data_with_errorbars():
    """argv: ['t.gp']
    t.gp:
        set table
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
        plot $d index 0 using 1:2:3 with yerrorbars
    """
    check("table.data_with_errorbars")


def test_data_missing_and_comments():
    """argv: ['t.gp']
    t.gp:
        set table
        $m << EOD
        # header
        1 1
        2 ?
        3 NaN
        
        4 4
        5 abc
        6 6
        EOD
        set datafile missing '?'
        plot $m
    """
    check("table.data_missing_and_comments")


def test_csv_separator():
    """argv: ['t.gp']
    t.gp:
        set table
        $c << EOD
        x,y,z
        1,2,3
        4,,6
        7,8,9
        EOD
        set datafile separator comma
        plot $c using 1:3, $c using 1:2
    """
    check("table.csv_separator")


def test_columnheader():
    """argv: ['t.gp']
    t.gp:
        set table
        $c << EOD
        name value other
        1 10 100
        2 20 200
        EOD
        plot $c using 1:2 title columnheader, $c using 1:3 title columnheader(3)
    """
    check("table.columnheader")


def test_named_columns():
    """argv: ['t.gp']
    t.gp:
        set table
        $c << EOD
        alpha beta
        1 10
        2 20
        EOD
        set key autotitle columnhead
        plot $c using 'alpha':'beta'
    """
    check("table.named_columns")


def test_time_data():
    """argv: ['t.gp']
    t.gp:
        set table
        $t << EOD
        2020-01-01 5
        2020-01-15 7
        2020-03-01 2
        EOD
        set xdata time
        set timefmt '%Y-%m-%d'
        set format x '%d/%m'
        plot $t using 1:2
    """
    check("table.time_data")


def test_table_to_datablock():
    """argv: ['t.gp']
    t.gp:
        set table
        set table $out
        set samples 4
        plot [0:3] x*x
        unset table
        print $out
        print |$out|
    """
    check("table.table_to_datablock")


def test_table_with_table_style():
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
        plot $d using 1:2:($1*$2) with table
    """
    check("table.table_with_table_style")


def test_table_with_table_format():
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
        set table separator comma
        plot $d using 1:($2/3) with table
    """
    check("table.table_with_table_format")


def test_splot_function():
    """argv: ['t.gp']
    t.gp:
        set table
        set isosamples 3
        set samples 3
        splot [0:1][0:1] x+y
    """
    check("table.splot_function")


def test_splot_data():
    """argv: ['t.gp']
    t.gp:
        set table
        $g << EOD
        0 0 1
        0 1 2
        
        1 0 3
        1 1 4
        EOD
        splot $g using 1:2:3
    """
    check("table.splot_data")


def test_parametric():
    """argv: ['t.gp']
    t.gp:
        set table
        set parametric
        set samples 5
        plot [0:pi] cos(t), sin(t)
    """
    check("table.parametric")


def test_polar():
    """argv: ['t.gp']
    t.gp:
        set table
        set polar
        set samples 5
        plot [0:pi] 1
    """
    check("table.polar")


def test_iteration_plot():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 3
        plot [0:2] for [n=1:3] x**n title sprintf('n=%d', n)
    """
    check("table.iteration_plot")


def test_histogram_style_table():
    """argv: ['t.gp']
    t.gp:
        set table
        $h << EOD
        A 3 4
        B 5 1
        C 2 6
        EOD
        set style data histograms
        plot $h using 2:xtic(1), '' using 3
    """
    check("table.histogram_style_table")


def test_boxes_and_steps():
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
        plot $d with boxes, $d with steps, $d with fsteps
    """
    check("table.boxes_and_steps")


def test_filledcurves_table():
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
        plot $d using 1:2:($2+1) with filledcurves
    """
    check("table.filledcurves_table")


def test_ranges_clip_data():
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
        set xrange [2:4.5]
        plot $d
    """
    check("table.ranges_clip_data")


def test_autoscale_extend_table():
    """argv: ['t.gp']
    t.gp:
        set table
        set samples 4
        plot [-1:1] 3*x
    """
    check("table.autoscale_extend_table")


def test_x2_y2_axes():
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
        plot $d axes x2y2, $d using 1:($2*10) axes x1y2
    """
    check("table.x2_y2_axes")


def test_sample_keyword():
    """argv: ['t.gp']
    t.gp:
        set table
        plot sample [0:1:0.25] x, [2:3:0.5] x**2
    """
    check("table.sample_keyword")


def test_dummy_variable():
    """argv: ['t.gp']
    t.gp:
        set table
        set dummy u
        set samples 3
        plot [0:2] u**3
    """
    check("table.dummy_variable")


def test_binary_operators_in_using():
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
        plot $d using 1:($2 > 5 ? $2 : NaN)
    """
    check("table.binary_operators_in_using")


def test_array_plot():
    """argv: ['t.gp']
    t.gp:
        set table
        array A = [5, 3, 8]
        plot A, A using 1:(A[$1]*2)
    """
    check("table.array_plot")


def test_string_column_xtic():
    """argv: ['t.gp']
    t.gp:
        set table
        $h << EOD
        mon 1
        tue 3
        wed 2
        EOD
        plot $h using 0:2:xtic(1) with table
    """
    check("table.string_column_xtic")
