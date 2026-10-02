"""Behavioural tests: cli (20 cases, golden outputs in golden/cli.json)."""
from eval.tests._harness import check


def test_version_long():
    """argv: ['--version']
    """
    check("cli.version_long")


def test_version_short():
    """argv: ['-V']
    """
    check("cli.version_short")


def test_help():
    """argv: ['--help']
    """
    check("cli.help")


def test_help_short():
    """argv: ['-h']
    """
    check("cli.help_short")


def test_unknown_option():
    """argv: ['--bogus']
    """
    check("cli.unknown_option")


def test_missing_script():
    """argv: ['nope.gp']
    """
    check("cli.missing_script")


def test_e_multiple():
    """argv: ['-e', 'a=2; b=3', '-e', 'print a*b']
    """
    check("cli.e_multiple")


def test_e_then_file():
    """argv: ['-e', 'x=5', 't.gp']
    t.gp:
        print x**2
    """
    check("cli.e_then_file")


def test_file_then_e():
    """argv: ['t.gp', '-e', 'print y']
    t.gp:
        y=7
    """
    check("cli.file_then_e")


def test_two_files():
    """argv: ['a.gp', 'b.gp']
    """
    check("cli.two_files")


def test_stdin_script():
    """argv: []
    stdin: "print 'stdin', 1+1\\nprint undefined_name\\nprint 'not reached'\\n"
    """
    check("cli.stdin_script")


def test_dash_stdin():
    """argv: ['-']
    stdin: "print 'dash'\\n"
    """
    check("cli.dash_stdin")


def test_exit_status():
    """argv: ['t.gp']
    t.gp:
        print 'a'
        exit status 3
        print 'b'
    """
    check("cli.exit_status")


def test_exit_error_message():
    """argv: ['t.gp']
    t.gp:
        print 'a'
        exit error "custom failure"
    """
    check("cli.exit_error_message")


def test_quit_in_middle():
    """argv: ['t.gp']
    t.gp:
        print 1
        quit
        print 2
    """
    check("cli.quit_in_middle")


def test_error_stops_script():
    """argv: ['t.gp']
    t.gp:
        print 1
        print 1/
        print 2
    """
    check("cli.error_stops_script")


def test_e_error_exit():
    """argv: ['-e', 'print sin()']
    """
    check("cli.e_error_exit")


def test_default_settings_flag():
    """argv: ['-d', 't.gp']
    t.gp:
        show samples
        show angles
    """
    check("cli.default_settings_flag")


def test_call_with_args():
    """argv: ['-c', 't.gp', 'first', '2nd arg', '3']
    t.gp:
        print ARGC, ARG0, ARG1, ARG2, ARG3
        print ARGV
    """
    check("cli.call_with_args")


def test_persist_ignored():
    """argv: ['-persist', '-e', "print 'ok'"]
    """
    check("cli.persist_ignored")
