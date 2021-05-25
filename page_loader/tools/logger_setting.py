"""Setting logging."""

import yaml
import logging
import logging.config


with open('./page_loader/logging_config/normal_mode.yml') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


def set_log_level(log_level):
    if log_level == 'DEBUG':
        with open('./page_loader/logging_config/debug_mode.yml') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
