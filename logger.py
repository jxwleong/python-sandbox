#import logging
import logging.config
import os
from colored_logger import ColorFormatter
#import coloredlogs

# logger = logging.getLogger(__name__)
# #coloredlogs.install(level='DEBUG', logger=logger)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s:%(filename)s<%(lineno)d>:%(message)s', 
#                               datefmt='%Y-%m-%d %H:%M:%S')


# file_handler = logging.FileHandler('output.log', mode='w')
# file_handler.setLevel(logging.WARNING)
# file_handler.setFormatter(formatter)


#color_handler = ColorFormatter(formatter)

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'minimal': {
            'format': '%(asctime)s:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },        
        'verbose': {
            'format': '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'color_format': {
            'class': 'logging.ColorFormatter',
            'format': '$COLOR%(levelname)s $RESET %(asctime)s $BOLD$COLOR%(name)s$RESET %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'color_format',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['default'],
        },
        'another.module': {
            'level': 'DEBUG',
        },
    },
}


logging.config.dictConfig(DEFAULT_LOGGING)

logging.debug('Hello, log')
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(color_formatter)

# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# os.system('color')
# logger.debug('TEST')
#os.system('color')
COLOR = {
    'HEADER': '\033[95m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'RED': '\033[91m',
    'ENDC': '\033[0m',
}
#logger.info(COLOR['HEADER'] + 'This is info'+ COLOR['ENDC'])