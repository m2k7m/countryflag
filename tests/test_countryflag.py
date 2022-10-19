from src import countryflag
from cli_test_helpers import ArgvContext, shell


def test_runas_module():
    """Can this package be run as a Python module?"""
    result = shell("python3 -m countryflag --help")
    assert result.exit_code == 0


def test_module():
    """Tests the Python module output"""
    expected = "🇫🇷 🇧🇪 🇯🇵 🇺🇸"
    actual = countryflag.getflag(
        ["France", "Belgium", "JP", "United States of America"]
    )
    assert actual == expected, "Output doesn't match with input countries!"


def test_entrypoint():
    """Is entrypoint script installed? (setup.py)"""
    result = shell("countryflag --help")
    assert result.exit_code == 0


def test_example_command():
    """
    Is command available?
    """
    result = shell("countryflag france --help")
    assert result.exit_code == 0
