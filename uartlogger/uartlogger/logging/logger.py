import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

from ..config.load import get_logging_config


def get_logger():
    """
    Returns a standard logger object. Ensures the logging handler is only
    created once

    Returns
    -------
    logger: logging.Logger
    """
    # grab the logger
    logger_name = "RH Logging"
    logger = logging.getLogger(logger_name)

    if len(logger.handlers) == 0:
        # set the format for the logger
        log_format = logging.Formatter(
            "%(asctime)s.%(msecs)03d [RH LOGGER] [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )

        # create and add the handlers
        sh = logging.StreamHandler()
        sh.setFormatter(log_format)
        logger.addHandler(sh)

    return logger


def get_rotating_file_name(self):
    """
    Returns the filename for the new file rotation

    Returns
    -------
    filename: str
        the new filename
    """
    base_path = os.path.join(
        os.path.expanduser("~"),
        "rh_logs"
    )

    if not os.path.isdir(base_path):
        os.mkdir(base_path)

    date = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    filename = os.path.join(
        base_path,
        f"{date}_rh.log"
    )

    return filename


def get_file_logger():
    """
    Returns a logger object for writing the RH to a local file

    Returns
    -------
    logger: logging.Logger
    """
    logger_name = "File Writer"
    logger = logging.getLogger(logger_name)
    config = get_logging_config()

    filename = get_rotating_file_name(None)

    if len(logger.handlers) == 0:
        # set the format for the logger
        log_format = logging.Formatter(
            "%(asctime)s.%(msecs)03d %(message)s",
            datefmt="%H:%M:%S"
        )
        fh = RotatingFileHandler(
            filename,
            maxBytes=config.getint("max_file_size"),
            backupCount=config.getint("num_backups")
        )
        fh.rotation_filename = get_rotating_file_name
        fh.setFormatter(log_format)
        logger.addHandler(fh)

    return logger

def set_LED_on():
    out="1"
    outb = out.encode("ascii")
    f = open("/sys/class/gpio/gpio156//value","wb")
    f.write(outb)
    f.close
    return 

def set_LED_off():
    out="0"
    outb = out.encode("ascii")
    f = open("/sys/class/gpio/gpio156//value","wb")
    f.write(outb)
    f.close
    return 

import urllib.request
def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False
print( 'connected' if connect() else 'no internet!' )