"""Module for working with files."""

import os
import logging
from page_loader.exceptions import FileError


logger = logging.getLogger(__name__)


def save_file(content, path, mode='w'):
    """Save file to at the specified path."""
    try:
        with open(path, mode) as file:
            file.write(content)
        logger.debug(f'File saved into {path}')
    except OSError as e:
        raise FileError(f'Directory "{path}" not found.\n{e}') from e


def read_file(path, mode='r'):
    """Open and read file to at the specified path."""
    try:
        with open(path, mode) as file:
            result = file.read()
        logger.debug(f'Read file from {path}')
    except OSError as e:
        raise FileError(f'File "{path}" not found.\n{e}') from e
    return result


def create_dir(dir_path):
    """Create a directory at the specified path."""
    try:
        os.mkdir(dir_path)
    except OSError as e:
        raise FileError(f'Directory "{dir_path}" already exists.\n{e}') from e
