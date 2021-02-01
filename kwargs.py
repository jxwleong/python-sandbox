def print_kwargs(**kwargs):
    if kwargs:
        print(kwargs)
        print(kwargs['key'])


print_kwargs(key='Hello World')