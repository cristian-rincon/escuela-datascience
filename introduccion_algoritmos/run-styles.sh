#!/usr/bin/sh

autopep8 --in-place --aggressive --aggressive ./**/*.py
autopep8 -riv --aggressive ./**/*.py
isort ./**/*.py --diff