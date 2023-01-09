sudo echo 156 > /sys/class/gpio/export
sudo chmod 777 /sys/class/gpio/gpio156/value
sudo mraa-gpio set 18 0
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
sudo chown rock:dialout /dev/ttyUSB1
sudo chmod a+rw /dev/ttyUSB1
