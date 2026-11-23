#!/usr/bin/env python3
"""Portable checks; no source downloads or private files required."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
commands = [
    [sys.executable, "scripts/check_integrity.py"],
    [sys.executable, "scripts/check_arguments.py"],
    [sys.executable, "sources/aer-audit/coding-audit.py"],
    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
]
for command in commands:
    subprocess.run(command, cwd=ROOT, check=True)
print("PASS: structural, bounded coding and mathematical checks; not scholarly approval.")
