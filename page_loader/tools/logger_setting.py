"""Setting logging."""

import os
import logging
import logging.config


def set_log_setting(log_level, log_path):
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'c_format': {
                'format': '%(levelname)s - %(message)s'
            },
            'f_format': {
                    'format': '%(asctime)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': log_level,
                'formatter': 'c_format',
                'stream': 'ext://sys.stdout'
            },
        },
        'loggers': {
            'logger': {
                'handlers': ['console'],
                'level': log_level,
                'propagate': False
            },
        },
        'root': {
            'level': log_level,
            'handlers': ['console'],
        },
    }

    if log_level == 'DEBUG':
        config['handlers']['file'] = {
            'class': 'logging.FileHandler',
            'level': log_level,
            'filename': os.path.join(log_path, 'file.log'),
            'formatter': 'f_format'
        }
        config['loggers']['logger']['handlers'] = ['console', 'file']
        config['root']['handlers'] = ['console', 'file']

    logging.config.dictConfig(config)
