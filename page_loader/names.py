"""Module for working with names."""

import re
import os
import logging
from urllib.parse import urlparse


logger = logging.getLogger(__name__)


def get_page_name(url):
    """Get page name from page url."""
    if not url.endswith('/'):
        url += '/'
    name_page = get_name(url)
    logger.debug(f'Generated the page name "{name_page}" from URL "{url}"')
    return name_page


def get_resource_name(url):
    """Get resource name from resource url."""
    name_resource = get_name(url)
    logger.debug(f'Generated filename "{name_resource}" from URL "{url}"')
    return name_resource


def get_name(url):
    url_without_scheme = urlparse(url).netloc + urlparse(url).path
    base, ext = os.path.splitext(url_without_scheme)
    name = re.sub(r'\W', r'-', base.rstrip('/')) + ext
    if not ext:
        name += '.html'
    return name
