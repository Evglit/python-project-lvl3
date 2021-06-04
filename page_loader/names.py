"""Module for working with names."""

import re
import os
import logging
from urllib.parse import urlparse


logger = logging.getLogger(__name__)


def get_file_name(url):
    """Get page or resource name from url."""
    path = urlparse(url).path
    url_without_scheme = urlparse(url).netloc + path
    base, _ = os.path.splitext(url_without_scheme)
    _, ext = os.path.splitext(path)
    name = re.sub(r'\W', r'-', base.rstrip('/')) + ext
    if not ext:
        name += '.html'
    logger.debug(f'Generated ename "{name}" from URL "{url}"')
    return name
