from multiprocessing import Pipe, Process
import time
from uartlogger.core.serial import Stream
from uartlogger.logging import get_logger, get_file_logger, set_LED_on, set_LED_off

class Manager:

    def __init__(self):
        self.logger = get_logger()
        self.logger.info("Starting")
        self.file_logger = get_file_logger()

        # create the streamer object to read from the serial bus
        self.stream = Stream()

        # instantiate the pipes for the data
        self.pipe_in, self.pipe_out = Pipe()

    def run(self):
        """
        Main run method. starts the serial stream and writes to the logger along
        with any onboard processing/analysing
        """

        # start the stream process
        stream_proc = Process(
            name="Streaming Process",
            target=self.stream.run,
            args=(self.pipe_out,)
        )
        stream_proc.start()

        # main logging loop
        gpio_path = "/sys/class/gpio/gpio156//value"

        set_LED_on(gpio_path)
        previous_time = time.time()
        while True:
            
            try:
                # check for any data
                current_time = time.time()
                elapsed_time = current_time - previous_time
                if elapsed_time >= 1:
                    set_LED_on(gpio_path)
                if self.pipe_in.poll():
                    previous_time = time.time()
                    f = open(gpio_path,"r")
                    data = f.read()
                    if data != 0:
                        set_LED_off(gpio_path)

		            # store the data
                    data = self.pipe_in.recv().decode('utf-8').strip()
                    self.logger.debug(data)
                    self.file_logger.info(data)

                    # turn on LED if looping empty data
                    if (len(data)<1):
                        set_LED_on(gpio_path)

                    # TODO: analyse the data with post processing objects



            except KeyboardInterrupt as e:
                self.logger.warning(e)
                break

        set_LED_on(gpio_path)

        self.logger.info("Closing serial stream")
        # send the flag to stop the serial process
        self.pipe_in.send(True)

        # join the process and complete
        stream_proc.join(timeout=10.0)
        self.logger.info("Finished")
