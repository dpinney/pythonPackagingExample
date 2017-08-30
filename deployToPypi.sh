#!/bin/sh
# Deploy this library to pypi.
# You'll need credentials first from https://pypi.python.org/pypi

python "setup.py" sdist
python "setup.py" register
python "setup.py" sdist upload
