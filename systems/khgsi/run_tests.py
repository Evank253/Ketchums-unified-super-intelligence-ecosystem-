"""Run KHGSI planning-kernel tests with the Python standard library."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
result = subprocess.run(
    [sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"],
    cwd=ROOT,
    check=False,
)
raise SystemExit(result.returncode)
