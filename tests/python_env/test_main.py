import click.testing
import pytest

from python_env.main import main


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds():
    result = runner.invoke(main)
    assert result.exit_code == 0
