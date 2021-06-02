"""Main module of page loader."""

import os
import logging
from bs4 import BeautifulSoup
from page_loader.files import save_file, create_dir
from page_loader.names import get_name_page
from page_loader.web_requests import get_web_response
from page_loader.resources import (
    find_resources, download_resources, replace_res_path)


logger = logging.getLogger(__name__)


def download(url, path_output):
    """Download the webpage and its resources at the specified path."""
    logger.debug('Started download of page.')
    url = url.rstrip('/')
    page = get_web_response(url)
    page_name = get_name_page(url)
    page_path = os.path.join(path_output, page_name)
    path_without_ext, _ = os.path.splitext(page_path)
    resource_path = path_without_ext + '_files'
    create_dir(resource_path)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    resources_for_download, tags_for_change = find_resources(
        page_soup, resource_path, url)
    download_resources(resources_for_download)
    new_page_soup = replace_res_path(page_soup, tags_for_change)
    save_file(new_page_soup.prettify(formatter="html5"), page_path)
    return page_path
