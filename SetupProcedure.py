"""

sudo apt-get update
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
git clone https://github.com/DanielQu1108/RHLogger.git
cd RHLogger
cd uartlogger
poetry install

sudo chown root:root /home/rock/RHLogger/uartlogger/rmsudo.sh
sudo chmod 700 /home/rock/RHLogger/uartlogger/rmsudo.sh

sudo visudo

Below the line: %sudo   ALL=(ALL:ALL) ALL, insert:
rock ALL=(ALL) NOPASSWD: /home/rock/RHLogger/uartlogger/rmsudo.sh

poetry run python3 -m /home/rock/RHLogger/uartlogger/main

"""