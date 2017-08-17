#!/bin/bash

exec env CORE_MODE=development \
    $(pwd)/_venv/bin/python $(pwd)/$1/main.py
