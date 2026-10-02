"""Behavioural tests: dumb (43 cases, golden outputs in golden/dumb.json)."""
from eval.tests._harness import check


def test_sin_default():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot sin(x)
    """
    check("dumb.sin_default")


def test_two_functions():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [-5:5] x**2/5, abs(x) title 'abs'
    """
    check("dumb.two_functions")


def test_small_canvas():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 40,12
        plot cos(x)
    """
    check("dumb.small_canvas")


def test_wide_canvas():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 120,30
        plot [0:20] sin(x)*x
    """
    check("dumb.wide_canvas")


def test_data_points():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        plot $d with points
    """
    check("dumb.data_points")


def test_data_linespoints():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        plot $d with linespoints title 'measurements'
    """
    check("dumb.data_linespoints")


def test_impulses():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        plot $d with impulses
    """
    check("dumb.impulses")


def test_boxes():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set boxwidth 0.5
        set style fill solid
        plot $d with boxes
    """
    check("dumb.boxes")


def test_histogram():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $h << EOD
        A 3 4
        B 5 1
        C 2 6
        EOD
        set style data histograms
        set style histogram clustered
        plot $h using 2:xtic(1) title 'one', '' using 3 title 'two'
    """
    check("dumb.histogram")


def test_steps():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        plot $d with steps
    """
    check("dumb.steps")


def test_errorbars():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
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
    check("dumb.errorbars")


def test_title_labels():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set title 'Main Title'
        set xlabel 'time (s)'
        set ylabel 'amplitude'
        plot sin(x)
    """
    check("dumb.title_labels")


def test_key_positions():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set key left bottom
        plot [0:5] x, 5-x
    """
    check("dumb.key_positions")


def test_key_outside_box():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set key outside right box
        plot [0:5] x, 5-x
    """
    check("dumb.key_outside_box")


def test_no_key_no_border():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        unset key
        unset border
        plot [0:3] x**2
    """
    check("dumb.no_key_no_border")


def test_grid():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set grid
        plot [0:10] sqrt(x)
    """
    check("dumb.grid")


def test_custom_tics():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xtics 0, 2, 10
        set ytics ('lo' -1, 'zero' 0, 'hi' 1)
        plot [0:10] sin(x)
    """
    check("dumb.custom_tics")


def test_mirror_off_and_out():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xtics nomirror out
        set ytics nomirror
        plot [0:6] exp(-x)
    """
    check("dumb.mirror_off_and_out")


def test_log_scale():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set logscale y
        plot [1:100] x**2
    """
    check("dumb.log_scale")


def test_log_both():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set logscale xy
        plot [1:1000] x**1.5
    """
    check("dumb.log_both")


def test_yrange_fixed():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set yrange [-2:2]
        plot tan(x)
    """
    check("dumb.yrange_fixed")


def test_negative_ranges():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [-100:-10] x
    """
    check("dumb.negative_ranges")


def test_tiny_values():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [0:1e-6] x*1e-6
    """
    check("dumb.tiny_values")


def test_huge_values():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [0:1e9] x**2
    """
    check("dumb.huge_values")


def test_format_tics():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set format y '%.1e'
        set format x '%.0f%%'
        plot [0:100] x/3
    """
    check("dumb.format_tics")


def test_time_axis():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $t << EOD
        2021-01-01 1
        2021-02-01 4
        2021-03-01 2
        2021-04-01 5
        EOD
        set xdata time
        set timefmt '%Y-%m-%d'
        set format x '%b'
        plot $t using 1:2 with linespoints
    """
    check("dumb.time_axis")


def test_labels_and_arrows():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set label 'peak' at 1.57,1
        set arrow from 0,0 to 3,0.5
        plot [0:3.14] sin(x)
    """
    check("dumb.labels_and_arrows")


def test_multiplot_layout():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set multiplot layout 1,2 title 'two'
        plot [0:3] x
        plot [0:3] -x
        unset multiplot
    """
    check("dumb.multiplot_layout")


def test_parametric_circle():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set parametric
        set size ratio -1
        plot [0:2*pi] cos(t), sin(t)
    """
    check("dumb.parametric_circle")


def test_polar_plot():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set polar
        plot [0:2*pi] 1+cos(t)
    """
    check("dumb.polar_plot")


def test_zero_axis():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set xzeroaxis
        set yzeroaxis
        plot [-3:3] x**3/10
    """
    check("dumb.zero_axis")


def test_y2_axis():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        set y2tics
        plot $d axes x1y1, $d using 1:($2*100) axes x1y2
    """
    check("dumb.y2_axis")


def test_filledcurves():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [0:3] x with filledcurves y=0
    """
    check("dumb.filledcurves")


def test_splot_surface():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set isosamples 10
        splot x*y
    """
    check("dumb.splot_surface")


def test_splot_hidden3d():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set hidden3d
        set isosamples 15
        splot [-2:2][-2:2] exp(-x**2-y**2)
    """
    check("dumb.splot_hidden3d")


def test_splot_view_map():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set view map
        set isosamples 8
        splot x+y
    """
    check("dumb.splot_view_map")


def test_contour():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set contour base
        set cntrparam levels 3
        unset surface
        set view map
        splot [-2:2][-2:2] x**2+y**2
    """
    check("dumb.contour")


def test_dumb_options_aspect():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 50,20 aspect 1,1
        plot [0:1] x
    """
    check("dumb.dumb_options_aspect")


def test_dumb_noenhanced_feed():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 60,18 noenhanced nofeed
        set title 'x_{sub}^2'
        plot [0:1] x
    """
    check("dumb.dumb_noenhanced_feed")


def test_point_types():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $d << EOD
        1 2.0
        2 4.1
        3 5.9
        4 8.2
        5 9.8
        6 12.3
        EOD
        plot $d using 1:2 with points pt 1, '' using 1:($2-2) with points pt 6
    """
    check("dumb.point_types")


def test_replot():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        plot [0:2] x
        replot x**2
    """
    check("dumb.replot")


def test_datafile_columns_plot():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        $c << EOD
        x a b
        1 1 3
        2 4 2
        3 9 1
        EOD
        set key autotitle columnhead
        plot for [i=2:3] $c using 1:i with lines
    """
    check("dumb.datafile_columns_plot")


def test_set_output_file():
    """argv: ['t.gp']
    t.gp:
        set term dumb size 79,24
        set output 'plot.txt'
        plot [0:1] x
        set output
        print 'written'
    """
    check("dumb.set_output_file")
