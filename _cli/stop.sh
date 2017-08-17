#!/bin/bash

echo "Stopping system..."
$(pwd)/_venv/bin/supervisorctl \
    -c $(pwd)/_base/supervisord.conf stop all
echo "System stopped."
