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

cd ..
cp startup.sh /home/rock/

sudo chmod 777 startup.sh

cd
sh startup.sh

sudo chmod 777 rh_logs

in /etc/rc.local, insert:

 ./home/rock/startup.sh 2>&1 >> /home/rock/start2.txt 

"""