"""Test for Page loader"""

from page_loader.download import download


def test_downlosd():
    assert download('https://ru.hexlet.io/courses', '/var/tmp') == '/var/tmp/ru-hexlet-io-courses.html'
