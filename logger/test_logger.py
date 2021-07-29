import logging
import logger

from logger_with_exception import foo

logger = logging.getLogger(__name__)

logger.info("test")
foo()
