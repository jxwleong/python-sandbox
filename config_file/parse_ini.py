# https://docs.python.org/3/library/configparser.html
import configparser
import os
import unittest

ROOT_DIR = os.path.dirname(__file__)

section_map = {
    "settings_fault": "Settings Fault",
    "settings_warning": "Settings Warning",
    "settings_overrides": "Settings Overrides"


}

config = configparser.ConfigParser()
# To preserve the case
# https://stackoverflow.com/a/1611877
config.optionxform = str
config.read(os.path.join(ROOT_DIR, "myconfig.ini"))

def get_section_values(section: str):
    """Extract key-values pair under section

    Args:
        section (str): section name in the config file

    Returns:
        [list]: List of key-values pair 
    """
    _list = []
    for key, value in config[section_map[section]].items():
        _list.append(f"{key}={value}")
    return _list

class Test_get_section_values(unittest.TestCase):
    def test_get_section_values_settings_fault_expect_return_correct_list(self):
        self.assertEqual(get_section_values("settings_fault"), ['foo=bar', 'user=jason'])

    def test_get_section_values_settings_fault_expect_return_correct_list(self):
        self.assertEqual(get_section_values("settings_warning"), ['warning=True'])

    def test_get_section_values_settings_fault_expect_return_correct_list(self):
        # Why .ini file is "Overrides=False" but function return "overrides=False"
        self.assertEqual(get_section_values("settings_overrides"), ['Overrides=False'])

if __name__ == "__main__":
    unittest.main()