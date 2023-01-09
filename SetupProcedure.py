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

cd
os.system("sudo /home/rock/RHLogger/uartlogger/rmsudo.sh")
sudo hwclock --set --date="2012-12-15 20:49:00"
sudo hwclock -s

sudo chmod 777 startup.sh
sh startup.sh

sudo chmod 777 rh_logs

in /etc/rc.local, insert:

sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

./home/rock/startup.sh 2>&1 >> /home/rock/start2.txt 



"""