import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-2s: %(message)s")

LOGGER = logging.getLogger()


def log(msg: str, level=logging.INFO):
    """Writes a message to the log"""
    LOGGER.log(level, msg)
