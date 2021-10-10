import time
import inspect
import logging

import unittest

def dict2str(dict_ :dict, remove_trailing_comma=True, exception=True) ->str:
    """
    Returns the dictionary's key value pair in the format
    "key=value, ..."

    Ex.
    dict_ = {a=123, b="lol"}
    str_ = "a=123, b='lol'"
    exception (bool): Set True will raise exception if dict len is 0\

    Arguments:
        dict_ (dict): Dictionary where the key and value pair
                      will be converted into string.
        remove_trailing_comma (bool): remove_trailing_comma (bool): Removed the trailing ", " of the str_
    Returns:
        str_ (str): String of the 'key=value' pair of dict_
    """
    str_ = ""
    if len(dict_) == 0:
        if exception is False:  return ""
        raise ValueError(f"Length of dict_ (dict_) is 0.")
    for key, value in dict_.items():
        str_ += f"{key}="
        if isinstance(value, str) is True:  str_ += f"'{value}', "
        else:   str_ += f"{value}, "
    if remove_trailing_comma is False: return str_
    return str_.rstrip(', ') # Removed trailing comma

class Test_dict2str(unittest.TestCase):
    def test_dict2str_one_element(self):
        self.assertEqual("logger=False", dict2str({"logger": False}))

    def test_dict2str_multiple_elements(self):
        self.assertEqual("unittest=1, key='haha', a='THe hell???'", dict2str({'unittest': 1, 'key': 'haha', 'a': 'THe hell???'}))

    def test_dict2str_given_empty_dict(self):
        self.assertRaises(ValueError, dict2str, {})


def tuple_element_to_str(tuple_ :tuple, remove_trailing_comma=True, exception=True) -> str:
    """
    Returns the dictionary's key value pair in the format
    "key=value, ..."

    Ex.
    tuple_ = (123, "lol")
    str_ = "123, 'lol'"
    
    Arguments:
        tuple_ (tuple): Tuple where the element
                        will be converted into string.
        remove_trailing_comma (bool): Removed the trailing ", " of the str_
        exception (bool): Set True will raise exception if tuple len is 0
    Returns:
        str_ (str): String of the 'element, ...' pair of tuple_
    """
    str_ = ""
    if len(tuple_) == 0:
        if exception is False:  return ""
        raise ValueError(f"Length of dict_ (dict_) is 0.")
    for element in tuple_:
        if isinstance(element, str) is True:  str_ += f"'{element}', "
        else:   str_ += f"{element}, "
    if remove_trailing_comma is False: return str_
    return str_.rstrip(', ') # Removed trailing comma

class Test_tuple_element_to_str(unittest.TestCase):
    def test_tuple_element_to_str_one_element(self):
        # Must have ", " if only one string element
        # Else will be treated as group of character when
        # iterated.
        # ('aaa') == 'aaa'
        self.assertEqual("'ABC'", tuple_element_to_str(("ABC", )))

    def test_tuple_element_to_str_multiple_elements(self):
        self.assertEqual("'HeLL', 'NO'", tuple_element_to_str(("HeLL", "NO")))

    def test_tuple_element_to_str_given_empty_tuple(self):
        self.assertRaises(ValueError, tuple_element_to_str, ())

def arguments_in_str():
    """
    Returns the arguments of caller in string
    Ex.
        def foo(logger, unittest=1, *args, **kwargs):
            print(arguments_in_str())
        Call: foo("", 2, 2, 3)
        Return: (logger='', unittest=2, 2, 3)

    Reference: https://kbyanc.blogspot.com/2007/07/python-aggregating-function-arguments.html
    """
    from inspect import getargvalues, stack
    a = getargvalues(stack()[1][0])
    b = stack()
    posname, kwname, args = getargvalues(stack()[1][0])[-3:]
    posargs = args.pop(posname, [])
    args.update(args.pop(kwname, []))
    #return args, posargs
    if len(posargs) == 0: 
        return "(" + dict2str(args) + ")"
    return "(" + \
            dict2str(args) + ", " +     \
            tuple_element_to_str(posargs) +     \
            ")"

def func2str(func, *args, **kwargs):
    """Return function with arguments in str

    Args:
        func (function reference): Function by reference

    Returns:
        str_ (str): Function in str

    Example:
        * func2str(foo, bar=a, bee=10)
        return "foo(bar=a, bee=10)"
    """
    argspec = inspect.getfullargspec(func)
    # This will raise exception if no arguments pass is
    # in wrong order/ wrong..
    inspect.getcallargs(func, *args, **kwargs)
    if (len(argspec.args) == 0 or \
        argspec.defaults is None) and \
            len(args) == 0 and \
            len(kwargs) == 0:
        str_ = ""
    elif len(args) == 0 and len(kwargs) == 0:
        str_ = ""
        for (arg, value) in zip(argspec.args, argspec.defaults):
            str_ += f"{arg}={value}, "
        str_ = str_.rstrip(", ")
    elif len(args) != 0 and len(kwargs) == 0:
        str_  = tuple_element_to_str(args)
    elif len(args) == 0 and len(kwargs) != 0:
        str_ = dict2str(kwargs)
    else:
        str_ = tuple_element_to_str(args, remove_trailing_comma=False)
        str_ += dict2str(kwargs)
    return f"{func.__name__}({str_})"

def function_wrapper(func, logger: logging.Logger=None):
    if logger is None:  log = print
    else:   log = logger.info
    def wrapper(*args, **kwargs):
        function_str = func2str(func, *args, **kwargs)
        log(f"{function_str} called.")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        log('{0} return {1}<{2}>'.format(function_str, type(result), result))
        return result
    return wrapper

# If len of args and kwargs is not
# Looks for default...
# Else direct look for kwargs or args...
@function_wrapper
def greet(name="Haha", *args, **kwargs):
    time.sleep(1)
    print('Hello {0}'.format(name))
    return 'Hello {0}'.format(name)

# greet()
# greet("a", 3, key="1")

@function_wrapper
def hreet(*args, **kwargs):
    time.sleep(1)
    return None

# hreet()
# hreet(1)
# hreet(key=1, a=2)
# hreet("aaa", key=1, a=2)

@function_wrapper
def temp():
    print("HAHA")

#temp()
def foo(bar="foo", foo=10, *args, **kwargs):
    pass

# print(func2str(foo))
# print(func2str(foo, 1))
# print(func2str(foo, "1"))
# print(func2str(foo, 2))
# print(func2str(foo, 1, 2, 'b', unittest="a"))
#if __name__ == "__main__":
    #unittest.main()

def function_wrapper2(func, logger: logging.Logger=None):
    if logger is None:  log = print
    else:   log = logger.info
    def wrapper(*args, **kwargs):
        args_str = tuple_element_to_str(args, exception=False)
        kwargs_str = dict2str(kwargs, exception=False)
        function_str = f"{func.__name__}({args_str}{kwargs_str})"
        log(function_str)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        #log('{0} return {1}<{2}>'.format(function_str, type(result), result))
        return result
    return wrapper

@function_wrapper2
def foo(bar, *args, **kwargs):
    print(args)
    print(kwargs)
    print("DAQU")
    pass

foo(bar=1)