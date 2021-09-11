import time
import sys

# for i in range(100):
#     i = i + 1
#     print("\rloading... %s%%" % i, end='')
#     time.sleep(.2)

toolbar_width = 40

# setup toolbar
# https://stackoverflow.com/a/3160819
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    print('■', end='', flush=True)
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar