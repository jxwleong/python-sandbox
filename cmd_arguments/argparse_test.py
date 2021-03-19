import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyvalue')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-d', '--data')
parser.add_argument('-f', '--file')

args = parser.parse_args()
print(args)