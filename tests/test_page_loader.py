"""Test for Page loader"""

from page_loader import download
from pathlib import Path
import requests_mock


def test_download(requests_mock):
    path_right_page = Path(Path(__file__).parent.absolute() / 'fixtures' / 'parislife.html')
    with open(path_right_page, 'r') as file:
        right_page = file.read()
    requests_mock.get('https://evglit.github.io', text=right_page)
    path_downloaded_page = download('https://evglit.github.io/')
    with open(path_downloaded_page, 'r') as file:
        downloaded_page = file.read()
    assert right_page == downloaded_page
