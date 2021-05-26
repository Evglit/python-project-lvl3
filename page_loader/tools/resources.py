"""Module for loading page resources."""

import os
import logging
from progress.bar import Bar
from urllib.parse import urlparse, urljoin
from page_loader.tools.names import get_name_resource
from page_loader.tools.files import save_file
from page_loader.tools.web_requests import get_web_response


logger = logging.getLogger(__name__)


def download_resources(page_soup, resource_dir_path, base_url, tag, attribute):
    """Download resources of page at the specified path."""
    logger.debug(f'Start downloading files of "{tag}" tag.')
    resource_tegs = page_soup.find_all(tag)
    bar = Bar(f'Loading files of {tag}', max=len(resource_tegs))
    for resource_tag in resource_tegs:
        resource_attr = resource_tag.get(attribute)
        if (urlparse(resource_attr).netloc == urlparse(base_url).netloc or # noqa: W504, E261, E501
                urlparse(resource_attr).netloc == ''):
            resource_url = urljoin(base_url, resource_attr).rstrip('/')
            response = get_web_response(resource_url)
            resource_name = get_name_resource(resource_url)
            resource_path = os.path.join(resource_dir_path, resource_name)
            save_file(response.content, resource_path, 'wb')
            resource_tag[attribute] = os.path.join(
                os.path.basename(resource_dir_path), resource_name)
        bar.next()
    bar.finish()
    return page_soup
