#!/bin/bash

source $(pwd)/_cli/stop.sh

source $(pwd)/_cli/_clean_bytecode.sh

echo "Restarting system..."
$(pwd)/_venv/bin/supervisorctl -c $(pwd)/_base/supervisord.conf \
    start all
echo "System restarted."
