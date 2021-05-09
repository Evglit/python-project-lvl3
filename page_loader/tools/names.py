"""Module for working with names."""

import re
import os
from urllib.parse import urlparse
from page_loader.tools.logger_setting import logger


def get_name_page(url):
    """Get page name from page url."""
    scheme = urlparse(url).scheme
    name_page = re.sub(f'{scheme}://', r'', url)
    name_page = re.sub(r'\W', r'-', name_page) + '.html'
    logger.debug(f'Generated the page name "{name_page}" from URL "{url}"')
    return name_page


def get_name_resource(url):
    """Get resource name from resource url."""
    scheme = urlparse(url).scheme
    name_resource = re.sub(f'{scheme}://', r'', url)
    base, ext = os.path.splitext(name_resource)
    name_resource = re.sub(r'\W', r'-', base) + ext
    logger.debug(f'Generated filename "{name_resource}" from URL "{url}"')
    return name_resource
