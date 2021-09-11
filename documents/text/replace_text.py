__author__ = "Jason Leong Xie Wei"
__email__ = "jason.xie.wei.leong@gmail.com"

import argparse
import re
import os
import sys
import logging
from collections import OrderedDict


dir_path = os.path.dirname(os.path.realpath(__file__))
recipe_path = os.path.join(dir_path, "recipe.py")
with open("debug.log", "w"):  pass
log_path = os.path.join(dir_path, "debug.log")

arg_dict = {
    "RECIPE_DICT\[\"Ingredient.A\"\]": 0,
    "RECIPE_DICT\[\"Ingredient.B\"\]": 0
    }

POSIX_PATTERN  = "\s*=\s*\"?\w*\"?"


def arg_init():
    """
    Initialize argparse
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--a_val', 
                       help=f"Value for recipe a", 
                       type=int)
    parser.add_argument('-b', '--b_val', 
                       help=f"Value for recipe b", 
                       type=int)                  
    args = parser.parse_args()
    return args


def process_arg(args):
    """
    Process the arguments(args) after calling arg_init()
    """
    global arg_dict

    args_dict = args.__dict__
    for index, (key, value) in enumerate(args_dict.items()):
        if value is not None:
            arg_key = list(arg_dict.keys())
            arg_value = list(arg_dict.values()) 
            arg_value[index] = value
            arg_dict = dict(zip(arg_key, arg_value))


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
        str: String read from file
    """
    with open(file, "r") as file:
        return file.read()
        

def write_file(file, data):
    """
    Write file with data, will overwrite old data!
    
    Args:
        file (str): Path to the file to be edited
        data (str): Data to be written to file
    """
    with open(file, "w") as file:
            file.write(data)


def replace_text(file, pattern, replacement, overwrite=False):
    """
    Replace the file content using re.sub

    Args:
        file (str): Path to the file to be edited
        pattern (str): Regex to search in file
        replacement (str): Replacement string for the "regexed" text in file
        overwrite (boolean): Overwrite the content of the file if set to True

    Returns:
        str: 
        if overwrite = True: Path of the file overwritten
        if overwrite = False: String of the updated file
    """
    file_data = read_file(file)
    match = re.search(pattern, file_data)

    if match is not None:
        result = re.sub(pattern,  replacement.replace("\\", ""), file_data)
        if overwrite == False:
            return result
        else:
            write_file(file, data=result)
            return file
    raise Exception(f"Cant find {pattern} in {file}")


logger = logger_init()
args = arg_init()
logger.info(f"Before process: {arg_dict}")
process_arg(args)
logger.info(f"After process: {arg_dict}")

try:
    file_data = read_file(recipe_path)
    logger.info("BEFORE:")
    logger.info(file_data)
    logger.info("AFTER:")

    for pattern_key, value in arg_dict.items():
        pattern = "".join([pattern_key, POSIX_PATTERN])
        replacement = "".join([pattern_key, " = ", str(value)])
        replace_text(recipe_path, pattern, replacement, overwrite=True)
    logger.info(f"New: {read_file(recipe_path)}")
except:
    logger.exception("Exception received!")