"""Main module of page loader."""

import os
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
    local_name_page = get_name_page(url)
    local_path_page = os.path.join(path_output, local_name_page)
    save_file(page.text, local_path_page)
    local_path_files = local_path_page.replace('.html', '_files')
    if not os.path.exists(local_path_files):
        os.mkdir(local_path_files)
    for teg, attribut in RESOURCES.items():
        download_resources(
            local_path_page, local_path_files,
            url, teg, attribut)
    return local_path_page
