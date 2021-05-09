"""Test for Page loader"""

import os
import pytest
import tempfile
import requests_mock
from pathlib import Path
from page_loader import download
from urllib.parse import urljoin
from page_loader.tools.files import read_file


'''PAGE_URL = 'https://site.com/blog/about'
HTML_FILE_NAME = 'site-com-blog-about.html'
ASSETS_DIR_NAME = 'site-com-blog-about_files'
BASE_URL = 'https://site.com/'
ASSETS = [
    {
        'url_path': '/blog/about/assets/styles.css',
        'file_name': 'site-com-blog-about-assets-styles.css'
    },
    
    {
        'url_path': '/blog/about',
        'file_name': 'site-com-blog-about.html'
    },

    {
        'url_path': '/photos/me.jpg',
        'file_name': 'site-com-photos-me.jpg'
    },

    {
        'url_path': 'https://site.com/assets/scripts.js',
        'file_name': 'site-com-assets-scripts.js'
    }
]'''

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
        'url_path': 'images/python.png',
        'file_name': 'evglit-github-io-images-python.png'
    },

    {
        'url_path': 'js/runtime.js',
        'file_name': 'evglit-github-io-js-runtime.js'
    }
]


def get_fixture_path(file_name):
    fixture_path = Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)
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
            os.path.join('expected', ASSETS_DIR_NAME, asset['file_name']),
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


'''def test_download(requests_mock):
    path_right_page = Path(Path(__file__).parent.absolute() / 'fixtures' / 'evglit-github-io.html')
    path_expected_page = Path(Path(__file__).parent.absolute() / 'fixtures' / 'expected' / 'evglit-github-io.html')
    path_image = Path(Path(__file__).parent.absolute() / 'fixtures' / 'expected' / 'evglit-github-io_files' / 'evglit-github-io-images-python.png')
    path_css = Path(Path(__file__).parent.absolute() / 'fixtures' / 'expected' / 'evglit-github-io_files' / 'evglit-github-io-css-style.css')
    path_js = Path(Path(__file__).parent.absolute() / 'fixtures' / 'expected' / 'evglit-github-io_files' / 'evglit-github-io-js-runtime.js')
    right_page = read_file(path_right_page)
    expected_page = read_file(path_expected_page)
    image = read_file(path_image, 'rb')
    css = read_file(path_css, 'rb')
    js = read_file(path_js, 'rb')
    requests_mock.get('https://evglit.github.io', text=right_page)
    requests_mock.get('https://evglit.github.io/images/python.png', content=image)
    requests_mock.get('https://evglit.github.io/css/style.css', content=css)
    requests_mock.get('https://evglit.github.io/js/runtime.js', content=js)
    with tempfile.TemporaryDirectory() as tmpdir:
        path_downloaded_page = download('https://evglit.github.io/', tmpdir)
        downloaded_page = read_file(path_downloaded_page)
        assert expected_page == downloaded_page


def test_local_file_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        local_path = download('https://evglit.github.io', tmpdir)
        assert os.path.exists(local_path)
        assert os.path.exists(local_path.replace('.html', '_files'))'''


"""def test_exception():
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            download('https://evglit.com', tmpdir)
        except Exception as e:
            assert 'HTTPSConnectionPool' in str(e)
"""


"""@pytest.mark.parametrize('code', [404, 500])
def test_response_with_error(requests_mock, code):
    url = urljoin(BASE_URL, str(code))
    requests_mock.get(url, status_code=code)
         
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(Exception):
            assert download(url, tmpdirname)
"""