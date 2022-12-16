#!/bin/bash
cd /home/rock/UploadSample/uartlogger

echo "Welcome"
export PATH="/home/rock/.local/bin/:$PATH"
poetry --version -v > /home/rock/startup.txt
poetry run python3 -m main -v >> /home/rock/startup.txt

# ./home/rock/startup.sh 2>&1 >> /home/rock/start2.txt in /etc/rc.local