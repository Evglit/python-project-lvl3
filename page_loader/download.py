"""Page loader"""

from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
import re
import os


RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def download(url, path_output=os.getcwd()):
    url = url.rstrip('/')
    page = requests.get(url)
    if page.status_code != 200:
        raise f'Error{page.status_code}'
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


def get_name_page(url):
    scheme = urlparse(url).scheme
    name_page = re.sub(f'{scheme}://', r'', url)
    name_page = re.sub(r'\W', r'-', name_page) + '.html'
    return name_page


def save_file(content, path, mode='w'):
    with open(path, mode) as file:
        file.write(content)


def download_resources(path_page, path_files, url_host, tag, attribute):
    with open(path_page) as file:
        page_html = file.read()
    soup = BeautifulSoup(page_html, "html.parser")
    tags_resource = soup.find_all(tag)
    for tag_resource in tags_resource:
        attr_resource = tag_resource.get(attribute)
        if (urlparse(attr_resource).netloc == urlparse(url_host).netloc or
                urlparse(attr_resource).netloc == ''):
            url_resource = urljoin(url_host, attr_resource).rstrip('/')
            response = requests.get(url_resource)
            name_resource = get_name_resource(url_resource)
            local_path_resource = os.path.join(path_files, name_resource)
            save_file(response.content, local_path_resource, 'wb')
            tag_resource[attribute] = os.path.relpath(local_path_resource)
    save_file(soup.prettify(formatter='html5'), path_page)


def get_name_resource(url):
    name_resource = re.sub(r'\?.*$', r'', os.path.basename(url))
    base, ext = os.path.splitext(name_resource)
    name_resource = re.sub(r'\W', r'-', base) + ext
    """if ext == '':
        name_resource += '.html'"""
    return name_resource
