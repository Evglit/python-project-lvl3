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
    parser.add_argument(
        '-l',
        '--log_level',
        help='set log level',
    )
    args = parser.parse_args()
    return args.url, args.output, args.log_level
