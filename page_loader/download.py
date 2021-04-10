"""Page loader"""


import requests
import re


def download(url, path_output):
    page = requests.get(url)
    path_file = get_path_file(url, path_output)
    file = open(path_file, 'w')
    file.write(page.text)
    return path_file


def get_path_file(url, path_output):
    file_name = re.sub(r'^https:\/\/', r'', url)
    file_name = re.sub(r'\W', r'-', file_name) + '.html'
    path_file = path_output + '/' + file_name
    return path_file
