#!/bin/sh
# Deploy this library to pypi.
# You'll need credentials first from https://pypi.python.org/pypi
# Needs update to https://packaging.python.org/tutorials/packaging-projects/

python "setup.py" sdist
python "setup.py" register
python "setup.py" sdist upload