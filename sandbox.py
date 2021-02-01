import logging
import sys

def test():
    logger = logging.getLogger()
    logger.info("This is info ")

a_logger = logging.getLogger()

a_logger.setLevel(logging.INFO)


output_file_handler = logging.FileHandler("output.log")

stdout_handler = logging.StreamHandler(sys.stdout)


a_logger.addHandler(output_file_handler)

a_logger.addHandler(stdout_handler)


test()


