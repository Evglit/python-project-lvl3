"""Test for Page loader"""

import os
import pytest
import tempfile
import requests_mock
from pathlib import Path
from page_loader import download
from page_loader.tools.files import read_file


def test_download(requests_mock):
    path_right_page = Path(Path(__file__).parent.absolute() / 'fixtures' / 'evglit-github-io.html')
    path_image = Path(Path(__file__).parent.absolute() / 'fixtures' / 'evglit-github-io_files' / 'python.png')
    path_css = Path(Path(__file__).parent.absolute() / 'fixtures' / 'evglit-github-io_files' / 'style.css')
    path_js = Path(Path(__file__).parent.absolute() / 'fixtures' / 'evglit-github-io_files' / 'runtime.js')
    right_page = read_file(path_right_page)
    image = read_file(path_image, 'rb')
    css = read_file(path_css, 'rb')
    js = read_file(path_js, 'rb')
    requests_mock.get('https://evglit.github.io', text=right_page)
    requests_mock.get('https://evglit.github.io/evglit-github-io_files/python.png', content=image)
    requests_mock.get('https://evglit.github.io/evglit-github-io_files/style.css', content=css)
    requests_mock.get('https://evglit.github.io/evglit-github-io_files/runtime.js', content=js)
    with tempfile.TemporaryDirectory() as tmpdir:
        path_downloaded_page = download('https://evglit.github.io/', tmpdir)
        downloaded_page = read_file(path_downloaded_page)
        assert right_page == downloaded_page


def test_local_file_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        local_path = download('https://evglit.github.io', tmpdir)
        assert os.path.exists(local_path)
        assert os.path.exists(local_path.replace('.html', '_files'))


def test_exception():
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            download('https://evglit.com', tmpdir)
        except Exception as e:
            assert 'HTTPSConnectionPool' in str(e)
