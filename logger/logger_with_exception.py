import logging
import logger

logger = logging.getLogger(__name__)

try:
    raise Exception("FAK!")
except:
    logger.exception("Exception!")
