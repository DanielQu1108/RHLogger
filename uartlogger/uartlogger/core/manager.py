from multiprocessing import Pipe, Process

from uartlogger.core.serial import Stream
from uartlogger.logging import get_logger, get_file_logger

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
        f = open("/sys/class/gpio/gpio156//value","r")
        data = f.read()
        f.close
        print(data)

        out="1"
        outb = out.encode("ascii")
        f = open("/sys/class/gpio/gpio156//value","wb")
        f.write(outb)
        f.close

        while True:

            try:
                # check for any data
                if self.pipe_in.poll():
                    f = open("/sys/class/gpio/gpio156//value","r")
                    data = f.read()
                    if data != 0:
                        out="0"
                        outb = out.encode("ascii")
                        f = open("/sys/class/gpio/gpio156//value","wb")
                        f.write(outb)
                        f.close

		    # store the data
                    data = self.pipe_in.recv().decode('utf-8').strip()
                    self.logger.debug(data)
                    self.file_logger.info(data)

                    # TODO: analyse the data with post processing objects

            except KeyboardInterrupt as e:
                self.logger.warning(e)
                break

        out="1"
        outb = out.encode("ascii")
        f = open("/sys/class/gpio/gpio156//value","wb")
        f.write(outb)
        f.close

        self.logger.info("Closing serial stream")
        # send the flag to stop the serial process
        self.pipe_in.send(True)

        # join the process and complete
        stream_proc.join(timeout=10.0)
        self.logger.info("Finished")
