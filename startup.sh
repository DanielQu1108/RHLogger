#!/bin/bash
cd /home/rock/RHLogger/uartlogger

echo "Welcome"
export PATH="/home/rock/.local/bin/:$PATH"
poetry --version
poetry run python3 -m main

# ./home/rock/startup.sh 2>&1 >> /home/rock/start2.txt in /etc/rc.local