"""Shim: this tool now lives in bookkit (../bookkit, or env BOOKKIT_HOME).

Configuration: book.toml. Equivalent: py -3 ../bookkit/bk.py build
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.abspath(os.environ.get("BOOKKIT_HOME") or os.path.join(ROOT, "..", "bookkit")))

from bookkit.cli import main  # noqa: E402

raise SystemExit(main(["--book", ROOT, "build", *sys.argv[1:]]))
