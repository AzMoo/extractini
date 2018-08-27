from extractini import __version__
from click.testing import CliRunner
from extractini.console import extract_from_inifile


def test_version():
    assert __version__ == '0.1.0'


def test_invalid_file():
    runner = CliRunner()
    result = runner.invoke(extract_from_inifile, ['fakefile', 'fakesection', 'fakeoption'])
    assert result.exit_code == 2


def test_invalid_section():
    runner = CliRunner()
    result = runner.invoke(extract_from_inifile, ['tests/test.ini', 'fakesection', 'fakeoption'])
    assert result.exit_code == 1
    assert "Error: No section: 'fakesection'" in result.output


def test_invalid_option():
    runner = CliRunner()
    result = runner.invoke(extract_from_inifile, ['tests/test.ini', 'default', 'fakeoption'])
    assert result.exit_code == 1
    assert "Error: No option 'fakeoption' in section: 'default'" in result.output


def test_valid():
    runner = CliRunner()
    result = runner.invoke(extract_from_inifile, ['tests/test.ini', 'default', 'firstoption'])
    assert result.exit_code == 0
    assert result.output == "stuff\n"
