"""Module for working with files."""

from page_loader.tools.logger_setting import logger


def save_file(content, path, mode='w'):
    """Save file to at the specified path."""
    with open(path, mode) as file:
        file.write(content)
    logger.debug(f'File saved into {path}')


def read_file(path, mode='r'):
    """Open and read file to at the specified path."""
    with open(path, mode) as file:
        result = file.read()
    logger.debug(f'Read file from {path}')
    return result
