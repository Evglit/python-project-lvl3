"""Main module of page loader."""

import os
from bs4 import BeautifulSoup
from page_loader.tools.files import save_file
from page_loader.tools.names import get_name_page
from page_loader.tools.logger_setting import logger
from page_loader.tools.resources import download_resources
from page_loader.tools.web_requests import get_web_response


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
    if not os.path.exists(resource_dir_path):
        os.mkdir(resource_dir_path)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    for teg, attribut in RESOURCES.items():
        page_soup = download_resources(
            page_soup, resource_dir_path,
            url, teg, attribut)
    save_file(page_soup.prettify(formatter="html5"), page_path)
    return page_path
