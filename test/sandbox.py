import logging
import sys

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}
logger = logging.getLogger()
logger.info(COLOR["GREEN"], "This is info ")

a_logger = logging.getLogger()

a_logger.setLevel(logging.INFO)


output_file_handler = logging.FileHandler("output.log")

stdout_handler = logging.StreamHandler(sys.stdout)


a_logger.addHandler(output_file_handler)

a_logger.addHandler(stdout_handler)



import colorama
#colorama.init()
start = "\033[1;31m"
end = "\033[0;0m"
print("File is: \033[1;31m '<placeholder>' + end")

#import os
#os.system("color")


print('\u001b[31;1m')
#print(COLOR["GREEN"], "Testing Green!!", COLOR["ENDC"])