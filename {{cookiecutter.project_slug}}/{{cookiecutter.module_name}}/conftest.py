"""Configuration for automated test suite, allows you to automatically
skip tests marked as slow unless you provide the --slow option
on the commandline when invoking pytest
"""

import pytest

def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true", help="run slow tests")