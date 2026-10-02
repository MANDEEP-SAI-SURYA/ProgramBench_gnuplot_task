"""Behavioural tests: show (65 cases, golden outputs in golden/show.json)."""
from eval.tests._harness import check


def test_default_xrange():
    """argv: ['t.gp']
    t.gp:
        show xrange
    """
    check("show.default_xrange")


def test_default_yrange():
    """argv: ['t.gp']
    t.gp:
        show yrange
    """
    check("show.default_yrange")


def test_default_samples():
    """argv: ['t.gp']
    t.gp:
        show samples
    """
    check("show.default_samples")


def test_default_angles():
    """argv: ['t.gp']
    t.gp:
        show angles
    """
    check("show.default_angles")


def test_default_style_data():
    """argv: ['t.gp']
    t.gp:
        show style data
    """
    check("show.default_style_data")


def test_default_style_function():
    """argv: ['t.gp']
    t.gp:
        show style function
    """
    check("show.default_style_function")


def test_default_key():
    """argv: ['t.gp']
    t.gp:
        show key
    """
    check("show.default_key")


def test_default_border():
    """argv: ['t.gp']
    t.gp:
        show border
    """
    check("show.default_border")


def test_default_logscale():
    """argv: ['t.gp']
    t.gp:
        show logscale
    """
    check("show.default_logscale")


def test_default_xtics():
    """argv: ['t.gp']
    t.gp:
        show xtics
    """
    check("show.default_xtics")


def test_default_ytics():
    """argv: ['t.gp']
    t.gp:
        show ytics
    """
    check("show.default_ytics")


def test_default_mxtics():
    """argv: ['t.gp']
    t.gp:
        show mxtics
    """
    check("show.default_mxtics")


def test_default_grid():
    """argv: ['t.gp']
    t.gp:
        show grid
    """
    check("show.default_grid")


def test_default_title():
    """argv: ['t.gp']
    t.gp:
        show title
    """
    check("show.default_title")


def test_default_xlabel():
    """argv: ['t.gp']
    t.gp:
        show xlabel
    """
    check("show.default_xlabel")


def test_default_size():
    """argv: ['t.gp']
    t.gp:
        show size
    """
    check("show.default_size")


def test_default_origin():
    """argv: ['t.gp']
    t.gp:
        show origin
    """
    check("show.default_origin")


def test_default_margin():
    """argv: ['t.gp']
    t.gp:
        show margin
    """
    check("show.default_margin")


def test_default_datafile():
    """argv: ['t.gp']
    t.gp:
        show datafile
    """
    check("show.default_datafile")


def test_default_zero():
    """argv: ['t.gp']
    t.gp:
        show zero
    """
    check("show.default_zero")


def test_default_clip():
    """argv: ['t.gp']
    t.gp:
        show clip
    """
    check("show.default_clip")


def test_default_offsets():
    """argv: ['t.gp']
    t.gp:
        show offsets
    """
    check("show.default_offsets")


def test_default_isosamples():
    """argv: ['t.gp']
    t.gp:
        show isosamples
    """
    check("show.default_isosamples")


def test_default_view():
    """argv: ['t.gp']
    t.gp:
        show view
    """
    check("show.default_view")


def test_default_palette():
    """argv: ['t.gp']
    t.gp:
        show palette
    """
    check("show.default_palette")


def test_default_colorbox():
    """argv: ['t.gp']
    t.gp:
        show colorbox
    """
    check("show.default_colorbox")


def test_default_boxwidth():
    """argv: ['t.gp']
    t.gp:
        show boxwidth
    """
    check("show.default_boxwidth")


def test_default_style_line():
    """argv: ['t.gp']
    t.gp:
        show style line
    """
    check("show.default_style_line")


def test_default_dummy():
    """argv: ['t.gp']
    t.gp:
        show dummy
    """
    check("show.default_dummy")


def test_default_encoding():
    """argv: ['t.gp']
    t.gp:
        show encoding
    """
    check("show.default_encoding")


def test_default_timefmt():
    """argv: ['t.gp']
    t.gp:
        show timefmt
    """
    check("show.default_timefmt")


def test_default_xdata():
    """argv: ['t.gp']
    t.gp:
        show xdata
    """
    check("show.default_xdata")


def test_default_fit():
    """argv: ['t.gp']
    t.gp:
        show fit
    """
    check("show.default_fit")


def test_default_loadpath():
    """argv: ['t.gp']
    t.gp:
        show loadpath
    """
    check("show.default_loadpath")


def test_default_bars():
    """argv: ['t.gp']
    t.gp:
        show bars
    """
    check("show.default_bars")


def test_default_pointsize():
    """argv: ['t.gp']
    t.gp:
        show pointsize
    """
    check("show.default_pointsize")


def test_default_polar():
    """argv: ['t.gp']
    t.gp:
        show polar
    """
    check("show.default_polar")


def test_default_parametric():
    """argv: ['t.gp']
    t.gp:
        show parametric
    """
    check("show.default_parametric")


def test_default_contour():
    """argv: ['t.gp']
    t.gp:
        show contour
    """
    check("show.default_contour")


def test_default_hidden3d():
    """argv: ['t.gp']
    t.gp:
        show hidden3d
    """
    check("show.default_hidden3d")


def test_default_minussign():
    """argv: ['t.gp']
    t.gp:
        show minussign
    """
    check("show.default_minussign")


def test_default_decimalsign():
    """argv: ['t.gp']
    t.gp:
        show decimalsign
    """
    check("show.default_decimalsign")


def test_default_tics():
    """argv: ['t.gp']
    t.gp:
        show tics
    """
    check("show.default_tics")


def test_default_autoscale():
    """argv: ['t.gp']
    t.gp:
        show autoscale
    """
    check("show.default_autoscale")


def test_default_jitter():
    """argv: ['t.gp']
    t.gp:
        show jitter
    """
    check("show.default_jitter")


def test_default_errorbars():
    """argv: ['t.gp']
    t.gp:
        show errorbars
    """
    check("show.default_errorbars")


def test_xrange_set():
    """argv: ['t.gp']
    t.gp:
        set xrange [-2.5:10]
        show xrange
        set xrange [*:5] reverse
        show xrange
    """
    check("show.xrange_set")


def test_key_set():
    """argv: ['t.gp']
    t.gp:
        set key top left box title 'Legend' font ',10' spacing 1.5
        show key
        unset key
        show key
    """
    check("show.key_set")


def test_logscale_set():
    """argv: ['t.gp']
    t.gp:
        set logscale xy 2
        set logscale z
        show logscale
        unset logscale y
        show logscale
    """
    check("show.logscale_set")


def test_tics_set():
    """argv: ['t.gp']
    t.gp:
        set xtics 0, 0.5, 3 rotate by 45 nomirror out
        set ytics ('low' 0, 'mid' 5, 'high' 10)
        show xtics
        show ytics
    """
    check("show.tics_set")


def test_label_set():
    """argv: ['t.gp']
    t.gp:
        set label 1 'first' at 1,2 center
        set label 'second' at graph 0.5,0.5 right rotate by 90
        set label 3 'x' at screen 0.1, second 2 front tc rgb 'red'
        show label
    """
    check("show.label_set")


def test_arrow_set():
    """argv: ['t.gp']
    t.gp:
        set arrow from 0,0 to 1,1
        set arrow 5 from graph 0,0 rto 1,2 nohead lw 2 dt 2
        show arrow
    """
    check("show.arrow_set")


def test_style_line_set():
    """argv: ['t.gp']
    t.gp:
        set style line 1 lc rgb '#ff0000' lw 2 pt 7 ps 1.5
        set style line 2 lt 3 dashtype '--'
        show style line
    """
    check("show.style_line_set")


def test_grid_set():
    """argv: ['t.gp']
    t.gp:
        set grid xtics mytics lt 0 lw 1, lt 2
        show grid
    """
    check("show.grid_set")


def test_margins_set():
    """argv: ['t.gp']
    t.gp:
        set lmargin 5
        set rmargin at screen 0.9
        set tmargin 0
        show margin
    """
    check("show.margins_set")


def test_multiple_ranges():
    """argv: ['t.gp']
    t.gp:
        set xrange [1:2]; set yrange [3:4]; set y2range [5:6]; set cbrange [7:8]
        show xrange
        show yrange
        show y2range
        show cbrange
    """
    check("show.multiple_ranges")


def test_timefmt_set():
    """argv: ['t.gp']
    t.gp:
        set xdata time
        set timefmt '%Y-%m-%d'
        set format x '%b %d'
        show xdata
        show timefmt
        show format
    """
    check("show.timefmt_set")


def test_datafile_set():
    """argv: ['t.gp']
    t.gp:
        set datafile separator ','
        set datafile missing 'NaN'
        set datafile commentschars '#!'
        show datafile
    """
    check("show.datafile_set")


def test_samples_isosamples():
    """argv: ['t.gp']
    t.gp:
        set samples 50, 60
        set isosamples 12
        show samples
        show isosamples
    """
    check("show.samples_isosamples")


def test_reset_restores():
    """argv: ['t.gp']
    t.gp:
        set xrange [1:2]
        set samples 10
        set key off
        reset
        show xrange
        show samples
        show key
    """
    check("show.reset_restores")


def test_save_settings_subset():
    """argv: ['t.gp']
    t.gp:
        set xrange [0:5]
        set title 'T'
        show title
        show xrange
    """
    check("show.save_settings_subset")


def test_show_all_style():
    """argv: ['t.gp']
    t.gp:
        set style data linespoints
        set style function impulses
        set style fill solid 0.5 border -1
        show style
    """
    check("show.show_all_style")


def test_boxwidth_set():
    """argv: ['t.gp']
    t.gp:
        set boxwidth 0.8 relative
        show boxwidth
        set boxwidth 2 absolute
        show boxwidth
    """
    check("show.boxwidth_set")


def test_view_set():
    """argv: ['t.gp']
    t.gp:
        set view 30, 120, 1.2, 0.8
        show view
        set view map
        show view
    """
    check("show.view_set")


def test_unset_and_show():
    """argv: ['t.gp']
    t.gp:
        unset border
        unset xtics
        unset title
        show border
        show xtics
        show title
    """
    check("show.unset_and_show")
