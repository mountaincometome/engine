#!/bin/bash

source $(pwd)/_cli/_clean_bytecode.sh
source $(pwd)/_cli/_clean_logs.sh

$(pwd)/_venv/bin/supervisord -c $(pwd)/_base/supervisord.conf

echo "Starting system..."
$(pwd)/_venv/bin/supervisorctl -c $(pwd)/_base/supervisord.conf \
    start all
echo "System started."
