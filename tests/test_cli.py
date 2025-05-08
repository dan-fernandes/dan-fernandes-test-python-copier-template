import subprocess
import sys

from dan_fernandes_test_python_copier_template import __version__


def test_cli_version():
    cmd = [
        sys.executable,
        "-m",
        "dan_fernandes_test_python_copier_template",
        "--version",
    ]
    assert subprocess.check_output(cmd).decode().strip() == __version__
