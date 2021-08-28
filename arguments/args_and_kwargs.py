
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
    print("\n\n\n")
    print(*args)
    # Can't print this
    # https://stackoverflow.com/a/39623954
    #print(**kwargs)    
    
    
foo("haha", 1, name="lol")
    