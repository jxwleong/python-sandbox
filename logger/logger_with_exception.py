import logging
import logger

logger = logging.getLogger(__name__)


def foo():
    raise Exception("FOO!")
try:
    #raise Exception("FAK!")
    foo()
except:
    logger.exception("Exception!")
