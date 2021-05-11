#!/usr/bin/env python3
"""Page loader script."""

import sys
from page_loader import download
from page_loader.tools.cli import parse_arg
from page_loader.tools.logger_setting import logger, config_logger


def main():
    url, path_output, log_level = parse_arg()
    try:
        config_logger(log_level)
        path = download(url, path_output)
        print(f'Page was successfully downloaded into {path}')
        sys.exit(0)
    except Exception as e:
        logger.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
