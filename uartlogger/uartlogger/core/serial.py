import serial
from time import sleep
from uartlogger.config import get_serial_config
from uartlogger.logging import get_logger


class Stream:

    def __init__(self):

        # set the config variables
        config = get_serial_config()
        self.port = config.get("port")
        self.reattempts = config.getint("reattempts")
        self.attempt_delay = config.getfloat("attempt_delay")
        self.baudrate = config.getfloat("baudrate")

        # initialise the serial bus
        self.ser = serial.Serial(
            baudrate=self.baudrate,
        )
        self.ser.port = self.port

        self.logger = get_logger()

    def run(self, pipe):
        """
        Method to manage the serial connection and read from the bus. Expected
        to be run as a separate process from the main analysis and writing
        functionality

        Parameters
        ----------
        pipe:
            Pipe to send the data back to the manager process
        """
        # connect to the serial bus
        self.connect()

        while True:
            # check if the serial port is connected
            if not self.ser.isOpen():
                self.connect()

            # try to read the data
            try:
                data = self.ser.readline()
            except Exception as e:
                self.logger.warning(e)
                self.connect()
                continue

            # send the data to the pipe
            pipe.send(data)

            if pipe.poll():
                # data received on the pipe assume we should close
                break

        self.ser.close()

    def connect(self):
        """
        Attempt to connect to the serial port. Allowing for mulitple connection
        attempts

        Raises
        ------
        ConnectionError:
            incase the maximum number of attempts to reconnect are exceeded
        """

        attempts = -1

        # ensure the serial connection is closed
        self.ser.close()
        while attempts < self.reattempts:

            # increment the counter only if reattempts is greater than 0
            # there 0 will be retry indefinitely
            if self.reattempts > 0:
                if attempts == -1:
                    attempts = 1
                else:
                    attempts += 1
                    out="1"
                    outb = out.encode("ascii")
                    f = open("/sys/class/gpio/gpio156//value","wb")
                    f.write(outb)
                    f.close

            self.logger.info(
                f"Attempting to connect with serial port: {self.port}")
            self.logger.info(f"Attempt {attempts} of {self.reattempts}")

            # reopen the serial connection
            try:
                self.ser.open()
            except Exception as e:
                self.logger.warning(e)
            finally:
                if self.ser.isOpen():
                    self.logger.info("Serial connection made")
                    return

            sleep(self.attempt_delay)

        # reached if the maximum number of attempts has been exceeded
        raise ConnectionError("Cannot connect to serial")
