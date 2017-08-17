#!/bin/bash

# Installing `PyPy3.5`
sudo apt-get update
wget -P /tmp \
    https://bitbucket.org/pypy/pypy/downloads/pypy3-v5.8.0-linux64.tar.bz2
mkdir $(pwd)/_pypy
tar xvjf /tmp/pypy3-v5.8.0-linux64.tar.bz2 -C $(pwd)/_pypy \
    --strip-components 1
rm /tmp/pypy3-v5.8.0-linux64.tar.bz2
# Setuping `virtualenv`
$(pwd)/_pypy/bin/pypy3 -m venv ./_venv
# Installing `pip3`'s packages
$(pwd)/_venv/bin/pip3 install --upgrade pip
source $(pwd)/_cli/install.sh
