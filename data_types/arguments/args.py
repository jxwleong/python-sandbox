"""
Example python script to demonstrate the use case of args
"""
def print_args(*args):
    if args:
        print(args)
        if 'GT2' in args or 'Gt1' in args:
            print('YES!')

print_args('GT2', 'Gt1')            