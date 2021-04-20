"""Page loader"""

from bs4 import BeautifulSoup
import requests
import re
import os


def download(url, path_output=os.getcwd()):
    page = requests.get(url)
    if page.status_code == 200:
        local_name = get_local_name(url)
        local_path_files = os.path.join(path_output, local_name) + '_files'
        if not os.path.exists(local_path_files):
            os.mkdir(local_path_files)
        page_html = download_imges(page.text, local_path_files)
        local_path_page = os.path.join(path_output, local_name) + '.html'
        with open(local_path_page, 'w') as file:
            file.write(page_html)
        return local_path_page
    raise f'Error: {page.status_code}'


def get_local_name(url):
    local_name = re.sub(r'^https:\/\/', r'', url)
    local_name = re.sub(r'\W', r'-', os.path.splitext(local_name)[0])\
        + os.path.splitext(local_name)[1]
    return local_name


def download_imges(page_html, local_path):
    soup = BeautifulSoup(page_html, "lxml")
    imgs = soup.find_all('img')
    for img in imgs:
        url_img = img.get('src')
        img_file = requests.get(url_img)
        img_name = os.path.basename(url_img)
        local_path_img = os.path.join(local_path, get_local_name(img_name))
        with open(local_path_img, 'wb') as file:
            file.write(img_file.content)
        page_html = re.sub(url_img, os.path.relpath(local_path_img), page_html)
    return page_html
