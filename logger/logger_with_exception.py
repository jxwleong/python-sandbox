import logging
import logger

logger = logging.getLogger(__name__)


def foo():
    logger.error("raise Exception!")
    raise Exception("FOO!")
try:
    #raise Exception("FAK!")
    foo()
except:
    logger.exception("Exception!")
