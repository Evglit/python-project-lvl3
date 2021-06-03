"""Main module of page loader."""

import os
import logging
from bs4 import BeautifulSoup
from page_loader.files import save_file, create_dir
from page_loader.names import get_name
from page_loader.web_requests import get_web_response
from page_loader.resources import (
    find_resource, download_resources, replace_res_path)


logger = logging.getLogger(__name__)


def download(url, output_path):
    """Download the webpage and its resources at the specified path."""
    logger.debug('Started download of page.')
    page = get_web_response(url)
    page_name = get_name(url)
    page_path = os.path.join(output_path, page_name)
    path_without_ext, _ = os.path.splitext(page_path)
    resource_path = path_without_ext + '_files'
    create_dir(resource_path)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    resources_for_download, tags_for_change = find_resource(
        page_soup, resource_path, url)
    download_resources(resources_for_download)
    replace_res_path(tags_for_change)
    save_file(page_soup.prettify(formatter="html5"), page_path)
    return page_path
