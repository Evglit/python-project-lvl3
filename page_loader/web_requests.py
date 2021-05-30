"""Module for web requests."""

import logging
import requests


logger = logging.getLogger(__name__)


def get_web_response(url):
    """Get web response at the specified url."""
    logger.debug(f'Request to {url}')
    response = requests.get(url)
    response.raise_for_status()
    logger.debug('The answer was received successfully.')
    return response
