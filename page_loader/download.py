"""Main module of page loader."""

import os
import logging
from bs4 import BeautifulSoup
from page_loader.tools.files import save_file
from page_loader.tools.names import get_name_page
from page_loader.tools.resources import find_resources, download_resources
from page_loader.change_page import replace_res_path
from page_loader.tools.web_requests import get_web_response


logger = logging.getLogger(__name__)


RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def download(url, path_output):
    """Download the webpage and its resources at the specified path."""
    logger.debug('Started download of page.')
    url = url.rstrip('/')
    page = get_web_response(url)
    page_name = get_name_page(url)
    page_path = os.path.join(path_output, page_name)
    resource_dir_path = page_path.replace('.html', '_files')
    os.mkdir(resource_dir_path)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    resources_for_download, tags_for_change = find_resources(
        page_soup, resource_dir_path, url, RESOURCES)
    download_resources(resources_for_download)
    new_page_soup = replace_res_path(page_soup, tags_for_change)
    save_file(new_page_soup.prettify(formatter="html5"), page_path)
    return page_path
