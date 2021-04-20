"""Test for Page loader"""

from page_loader import download
import requests
import requests_mock
from pathlib import Path
from bs4 import BeautifulSoup


def test_download(requests_mock):
    path_right_page = Path(Path(__file__).parent.absolute() / 'fixtures' / 'parislife-ru-blog_files.html')
    with open(path_right_page, 'r') as file:
        right_page = file.read()
    requests_mock.get('https://parislife.ru/blog', text=right_page)
    path_downloaded_page = download('https://parislife.ru/blog')
    with open(path_downloaded_page, 'r') as file:
        downloaded_page = file.read()
    assert right_page == downloaded_page
