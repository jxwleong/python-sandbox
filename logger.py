import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s', 
                              datefmt='%Y-%m-%d %H:%M:%S')

file_handler = logging.FileHandler('output.log', mode='w')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.warning('TEST')