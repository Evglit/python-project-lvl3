"""Setting logging."""

import os
import logging


# Create a logger
logger = logging.getLogger(__name__)

# Set logger level
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handlers to the logger
logger.addHandler(c_handler)


def config_logger(log_level, path_output):
    c_handler.setLevel(log_level)
    log_path = os.path.join(path_output, 'file.log')
    f_handler = logging.FileHandler(log_path)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
