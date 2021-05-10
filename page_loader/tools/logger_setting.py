"""Setting logging."""

import os
import logging

# Create a logger
logger = logging.getLogger(__name__)


def configure_logger(log_level, paht):
    # Set logger level
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(os.path.join(paht, 'file.log'))
    c_handler.setLevel(log_level)
    f_handler.setLevel('DEBUG')

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
