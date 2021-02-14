import time
import sys

for i in range(100):
    i = i + 1
    print("\rloading... %s%%" % i, end='')
    time.sleep(.2)
