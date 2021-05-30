"""Module for working with files."""

import logging
from page_loader.custom_exceptions import FileError


logger = logging.getLogger(__name__)


def save_file(content, path, mode='w'):
    """Save file to at the specified path."""
    try:
        with open(path, mode) as file:
            file.write(content)
        logger.debug(f'File saved into {path}')
    except Exception as e:
        raise FileError(f'Error saving file.\n{e}') from e


def read_file(path, mode='r'):
    """Open and read file to at the specified path."""
    try:
        with open(path, mode) as file:
            result = file.read()
        logger.debug(f'Read file from {path}')
    except Exception as e:
        raise FileError(f'Error opening file.\n{e}') from e
    return result
