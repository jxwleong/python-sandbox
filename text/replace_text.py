__author__ = "Jason Leong Xie Wei"
__email__ = "jason.xie.wei.leong@gmail.com"

import re
import os
import sys
import logging


dir_path = os.path.dirname(os.path.realpath(__file__))
recipe_path = os.path.join(dir_path, "recipe.py")
log_path = os.path.join(dir_path, "debug.log")

def logger_init():
    """
    Initialize and return logger
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s"))
    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s"))
    logger.addHandler(stdout_handler)

    return logger


def read_file(file):
    """
    Read and return the context of file in str format

    Args:
        file (str): Path to the file to be read

    Returns:
        str: string read from file
    """
    with open(file, "r") as file:
        return file.read()


logger = logger_init()


pattern = "RECIPE_DICT\[\"Ingredient.B\"\]\s*=\s*\"\w*\""
#pattern = "/s/s/s/s/"

try:
    file_data = read_file(recipe_path)
    logger.info("BEFORE:")
    logger.info(file_data)
    logger.info("AFTER:")

    match = re.search(pattern, file_data)
    if match is not None:
        logger.info(f"Match found! {match}")
        result = re.sub(pattern, "RECIPE_DICT[\"Ingredient.B\"] = \"Juice\"", file_data)
        logger.info(result)
    else:
        logger.warning(f"Match not found")
except:
    logger.exception("Exception received!")