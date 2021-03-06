#!/usr/bin/env python3
"""Page loader script."""

import sys
import logging
from page_loader import download
from page_loader.cli import parse_arg
from page_loader.logger_setting import set_log_setting
from page_loader.exceptions import AppInternalError


logger = logging.getLogger(__name__)


def main():
    url, output_path, log_level = parse_arg()
    try:
        set_log_setting(log_level, output_path)
        page_path = download(url, output_path)
        print(f'Page was successfully downloaded into {page_path}')
        sys.exit(0)
    except AppInternalError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
