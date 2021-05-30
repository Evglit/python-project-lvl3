"""Test for Page loader"""

import os
import pytest
import tempfile
from pathlib import Path
from page_loader import download
from urllib.parse import urljoin
from page_loader.files import read_file
from page_loader.custom_exceptions import AppInternalError


PAGE_URL = 'https://evglit.github.io/'
HTML_FILE_NAME = 'evglit-github-io.html'
ASSETS_DIR_NAME = 'evglit-github-io_files'
BASE_URL = 'https://evglit.github.io/'
ASSETS = [
    {
        'url_path': 'css/style.css',
        'file_name': 'evglit-github-io-css-style.css'
    },

    {
        'url_path': 'https://evglit.github.io/images/python.png',
        'file_name': 'evglit-github-io-images-python.png'
    },

    {
        'url_path': 'js/runtime.js',
        'file_name': 'evglit-github-io-js-runtime.js'
    }
]


def get_fixture_path(file_name):
    fixture_path = Path(
        Path(__file__).parent.absolute() / 'fixtures' / file_name
    )
    return fixture_path


def get_fixture_data(file_name):
    fixture_path = get_fixture_path(file_name)
    fixture_data = read_file(fixture_path)
    return fixture_data


def test_page_load(requests_mock):
    content = get_fixture_data(HTML_FILE_NAME)
    requests_mock.get(PAGE_URL, text=content)
    expected_html_file_path = get_fixture_path(
        os.path.join('expected', HTML_FILE_NAME),
    )
    expected_html_content = read_file(expected_html_file_path)

    for asset in ASSETS:
        asset_url = urljoin(BASE_URL, asset['url_path'])
        expected_asset_path = get_fixture_path(
            os.path.join('expected', ASSETS_DIR_NAME, asset['file_name'])
        )
        expected_asset_content = read_file(expected_asset_path, 'rb')
        asset['content'] = expected_asset_content
        requests_mock.get(asset_url, content=expected_asset_content)

    with tempfile.TemporaryDirectory() as tmpdirname:
        assert not os.listdir(tmpdirname)

        output_file_path = download(PAGE_URL, tmpdirname)
        assert len(os.listdir(tmpdirname)) == 2
        assert len(os.listdir(os.path.join(tmpdirname, ASSETS_DIR_NAME))) == 3

        html_file_path = os.path.join(tmpdirname, HTML_FILE_NAME)
        assert output_file_path == html_file_path

        html_content = read_file(html_file_path)
        assert html_content == expected_html_content

        for asset in ASSETS:
            asset_path = os.path.join(
                tmpdirname, ASSETS_DIR_NAME, asset['file_name'])
            asset_contend = read_file(asset_path, 'rb')
            assert asset_contend == asset['content']


@pytest.mark.parametrize('code', [404, 500])
def test_response_with_error(requests_mock, code):
    url = urljoin(BASE_URL, str(code))
    requests_mock.get(url, status_code=code)
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(AppInternalError):
            assert download(url, tmpdirname)


def test_local_file_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        local_path = download('https://evglit.github.io', tmpdirname)
        assert os.path.exists(local_path)
        assert os.path.exists(local_path.replace('.html', '_files'))


def test_exception():
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(AppInternalError):
            download('https://evglit.com', tmpdirname)
