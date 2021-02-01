def print_args(*args):
    if args:
        print(args)
        if 'GT2' in args or 'Gt1' in args:
            print('YES!')