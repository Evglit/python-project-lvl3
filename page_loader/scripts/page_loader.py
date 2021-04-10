#!/usr/bin/env python3


from page_loader import download
from page_loader.tools.argparse import parse_arg


def main():
    url, path_output = parse_arg()
    print(download(url, path_output))


if __name__ == '__main__':
    main()
