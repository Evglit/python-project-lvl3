"""Module for web requests."""

import requests
from page_loader.tools.logger_setting import logger


def get_web_response(url):
    """Get web response at the specified url."""
    logger.debug(f'Request to {url}')
    response = requests.get(url)
    logger.debug('The answer was received successfully.')
    return response
