import unittest
import logging
import sys

logging.basicConfig(
     filename='log_file_name.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


 # set up logging to console
console = logging.StreamHandler(sys.stderr)
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
 
class MyTest(unittest.TestCase):
    def runTest(self):
        log = logging.getLogger(__name__)
        log.warning("debug message")
        self.assertEqual(1, 1)

unittest.TextTestRunner().run(MyTest())

