import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time', type=int)
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-d', '--data')
parser.add_argument('-f', '--file')

args = parser.parse_args()
print(args)

def is_optional_argument_specified(argument):
    """Assume argument w/o action"""
    if argument is None:
        return False
    return True

if is_optional_argument_specified(args.time):
    print("Delay time: %d" % args.time)
    time.sleep(args.time)