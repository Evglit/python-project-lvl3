"""Module for web requests."""

import os
import requests
from page_loader.tools.logger_setting import logger


def get_web_response(url):
    """Get web response at the specified url."""
    logger.debug(f'Request to {url}')
    code = os.path.basename(url)
    if code == '404' or code == '500':
        raise Exception(f'{code}')
    response = requests.get(url)
    logger.debug('The answer was received successfully.')
    return response
