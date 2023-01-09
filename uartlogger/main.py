import os
import logging
from uartlogger.config.load import get_logging_config
from uartlogger.core.manager import Manager
from uartlogger.logging.logger import get_logger, get_file_logger, connect_wifi
from uartlogger.logging import set_LED_on

def main():
    os.system("sudo /home/rock/RHLogger/uartlogger/rmsudo.sh")
    log_level = get_logging_config().getint("term_level")
    logger = get_logger()
    if log_level == 0:
        logger.setLevel(logging.DEBUG)
    elif log_level == 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    file_logger = get_file_logger()
    file_logger.setLevel(logging.DEBUG)

    gpio_path = "/sys/class/gpio/gpio156//value"
    set_LED_on(gpio_path)
    connect_wifi()
    manager = Manager()
    manager.run()


if __name__ == "__main__":
    main()
