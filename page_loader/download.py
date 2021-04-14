"""Page loader"""


import requests
import re
import os


def download(url, path_output=os.getcwd()):
    page = requests.get(url)
    if page.status_code == 200:
        path_file = get_path_file(url, path_output)
        with open(path_file, 'w') as file:
            file.write(page.text)
        return path_file
    return f'Error: {page.status_code}'


def get_path_file(url, path_output):
    file_name = re.sub(r'^https:\/\/', r'', url)
    file_name = re.sub(r'\W', r'-', file_name) + '.html'
    path_file = os.path.join(path_output, file_name)
    return path_file
