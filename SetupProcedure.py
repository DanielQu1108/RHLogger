"""

sudo apt-get update
sudo apt-get install python3-distutils
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
git clone https://github.com/DanielQu1108/RHLogger.git
cd RHLogger
cd uartlogger
poetry install
sudo apt-get install libmraa
sudo chown root:root /home/rock/RHLogger/uartlogger/rmsudo.sh
sudo chmod 700 /home/rock/RHLogger/uartlogger/rmsudo.sh

sudo visudo

Below the line: %sudo   ALL=(ALL:ALL) ALL, insert:
rock ALL=(ALL) NOPASSWD: /home/rock/RHLogger/uartlogger/rmsudo.sh

cd
sudo nano startup.sh

#!/bin/bash
cd /home/rock/RHLogger/uartlogger

echo "Welcome"
export PATH="/home/rock/.local/bin/:$PATH"
poetry --version -v > /home/rock/startup.txt
poetry run python3 -m main -v >> /home/rock/startup.txt


sudo chmod 777 startup.sh

in /etc/rc.local, insert:

 ./home/rock/startup.sh 2>&1 >> /home/rock/start2.txt 

"""