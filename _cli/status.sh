#!/bin/bash

$(pwd)/_venv/bin/supervisorctl \
    -c $(pwd)/_base/supervisord.conf status
