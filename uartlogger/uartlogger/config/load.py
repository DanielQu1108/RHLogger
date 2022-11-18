from modulefinder import IMPORT_NAME
import pathlib
import configparser
import os


def get_config_root() -> str:
    """
    Returns the path to the config folder

    Returns
    -------
    path: str
        The full path to the config folder
    """

    path = pathlib.Path(__file__).parent.absolute()

    return path


def get_config() -> configparser.ConfigParser:
    """
    Returns the config for the rh logger

    Returns
    -------
    config
    """
    user_path = os.path.expanduser("~")
    config_paths = [
        os.path.join(
            get_config_root(),
            "default.ini"
        ),
        os.path.join(
            user_path,
            ".rhconfig.ini"
        )
    ]

    config = configparser.ConfigParser()
    config.read(config_paths)

    return config


def get_serial_config() -> configparser.SectionProxy:
    """
    Returns the configuration for the serial connection

    Returns
    -------
    section:
        the serial section of the config
    """
    return get_config()["serial"]


def get_logging_config() -> configparser.SectionProxy:
    """
    Returns the configuration for the logging

    Returns
    -------
    section:
        the logging section of the config
    """
    return get_config()["logging"]
