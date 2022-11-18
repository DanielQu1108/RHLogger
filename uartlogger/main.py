import logging
from uartlogger.config.load import get_logging_config
from uartlogger.core.manager import Manager
from uartlogger.logging.logger import get_logger, get_file_logger


def main():
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

    manager = Manager()
    import urllib.request
    def connect():
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
    print( 'connected' if connect() else 'no internet!' )
    manager.run()


if __name__ == "__main__":
    main()
