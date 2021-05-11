"""Parser of arguments."""

import os
import argparse


def parse_arg():
    """Create argument parser."""
    parser = argparse.ArgumentParser(description='This utility downloads \
        pages from the Internet.')
    parser.add_argument('url', type=str)
    parser.add_argument(
        '-o',
        '--output',
        default=os.getcwd(),
        type=str,
        help='output dir (default: "/app")'
    )
    args = parser.parse_args()
    return args.url, args.output
