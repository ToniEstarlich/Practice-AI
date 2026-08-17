import subprocess
import sys

from .filesystem import WORKSPACE


def run_python(path: str):

    result = subprocess.run(
        [sys.executable, path],
        cwd=WORKSPACE,
        capture_output=True,
        text=True,
        timeout=30,
    )

    return {
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }