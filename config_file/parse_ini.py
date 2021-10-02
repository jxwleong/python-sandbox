# https://docs.python.org/3/library/configparser.html
import configparser

import os
ROOT_DIR = os.path.dirname(__file__)

config = configparser.ConfigParser()
a = config.read(os.path.join(ROOT_DIR, "myconfig.ini"))


print(config.sections())

_list = []
for key, value in config["Settings Fault"].items():
    print(f"{key}={value}")
    _list.append(f"{key}={value}")

print(_list)