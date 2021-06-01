"""Module for web requests."""

import logging
import requests
from page_loader.exceptions import RequestError


logger = logging.getLogger(__name__)


def get_web_response(url):
    """Get web response at the specified url."""
    logger.debug(f'Request to {url}')
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.debug('The answer was received successfully.')
    except requests.exceptions.RequestException as e:
        raise RequestError(
            f'Error when requesting {url}\n{e}') from e
    return response


def get_web_resource(url, path):
    """Get a resource and save it in chunks along the specified path."""
    logger.debug(f'Request resource by {url}')
    response = requests.get(url, stream=True)
    with open(path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1000):
            file.write(chunk)
    logger.debug('The resource was saved successfully.')
