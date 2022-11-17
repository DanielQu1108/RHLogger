sudo echo 156 > /sys/class/gpio/export
sudo chmod 777 /sys/class/gpio/gpio156/value
sudo mraa-gpio set 18 0

sudo chown rock:dialout /dev/ttyUSB1
sudo chmod a+rw /dev/ttyUSB1
