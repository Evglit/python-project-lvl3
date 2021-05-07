"""Module for loading page resources."""

import os
from bs4 import BeautifulSoup
from progress.bar import Bar
from urllib.parse import urlparse, urljoin
from page_loader.tools.logger_setting import logger
from page_loader.tools.names import get_name_resource
from page_loader.tools.files import save_file, read_file
from page_loader.tools.web_requests import get_web_response


def download_resources(path_page, path_files, url_host, tag, attribute):
    """Download resources of page at the specified path."""
    logger.debug(f'Start downloading files of "{tag}" tag.')
    page_html = read_file(path_page)
    soup = BeautifulSoup(page_html, "html.parser")
    tags_resource = soup.find_all(tag)
    bar = Bar(f'Loading files of {tag}', max=len(tags_resource))
    for tag_resource in tags_resource:
        attr_resource = tag_resource.get(attribute)
        if (urlparse(attr_resource).netloc == urlparse(url_host).netloc or # noqa: W504, E261, E501
                urlparse(attr_resource).netloc == ''):
            url_resource = urljoin(url_host, attr_resource).rstrip('/')
            response = get_web_response(url_resource)
            name_resource = get_name_resource(url_resource)
            local_path_resource = os.path.join(path_files, name_resource)
            save_file(response.content, local_path_resource, 'wb')
            tag_resource[attribute] = os.path.join(
                os.path.basename(path_files), name_resource)
        bar.next()
    save_file(soup.prettify(formatter='html5'), path_page)
    bar.finish()
