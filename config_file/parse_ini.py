# https://docs.python.org/3/library/configparser.html
import configparser

import os
ROOT_DIR = os.path.dirname(__file__)

config = configparser.ConfigParser()
a = config.read(os.path.join(ROOT_DIR, "myconfig.ini"))


print(config.sections())
