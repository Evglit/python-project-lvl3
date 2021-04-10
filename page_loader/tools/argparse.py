"""It parses arguments."""

import argparse
import os


def parse_arg():
    """It parses arguments."""
    parser = argparse.ArgumentParser(description='This utility downloads \
        pages from the Internet.')
    parser.add_argument('url')
    default_path = os.getcwd()
    parser.add_argument('-o', '--output', default=default_path,
                        help='output dir (default: "/app")')
    args = parser.parse_args()
    return args.url, args.output
