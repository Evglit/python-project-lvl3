"""Module for working with names."""

import re
import os
from urllib.parse import urlparse
from page_loader.tools.logger_setting import logger


def get_name_page(url):
    """Get page name from page url."""
    name_page = re.sub(r'\W', r'-', delete_scheme(url)) + '.html'
    logger.debug(f'Generated the page name "{name_page}" from URL "{url}"')
    return name_page


def get_name_resource(url):
    """Get resource name from resource url."""
    base, ext = os.path.splitext(delete_scheme(url))
    name_resource = re.sub(r'\W', r'-', base) + ext
    if not ext:
        name_resource += '.html'
    logger.debug(f'Generated filename "{name_resource}" from URL "{url}"')
    return name_resource


def delete_scheme(url):
    return urlparse(url).netloc + urlparse(url).path
