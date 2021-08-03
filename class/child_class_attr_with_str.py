import functools
import unittest

class Employee:
    def __init__(self, name, age):
        self.name = name
        # _age to prevent circular call
        # https://stackoverflow.com/questions/51341576/variables-starting-with-underscore-for-property-decorator
        self.age = age

class Engineer(Employee):
    def __init__(self, name, age, qualification):
        super().__init__(name, age)
        self.qualification = qualification

# Reference: https://stackoverflow.com/a/31174427
def rsetattr(obj, attr, val):
    pre, _, post = attr.rpartition('.')
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)

# using wonder's beautiful simplification: https://stackoverflow.com/questions/31174295/getattr-and-setattr-on-nested-objects/31174427?noredirect=1#comment86638618_31174427

def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('.'))

def get_attr(dotted_path):
    try:
        class_name, attribute = dotted_path.split('.', 1)
        return rgetattr(globals()[class_name], attribute)
    except:
        raise Exception(f"Received invalid dotted path '{dotted_path}'")

    obj_type = type(dotted_path)
    print(dotted_path)
    temp_obj = obj_type()
    return "Haha"

def set_attr(dotted_path, value):
    try:
        class_name, attribute = dotted_path.split('.', 1)
        return rsetattr(globals()[class_name], attribute, value)
    except:
        raise Exception(f"Received invalid dotted path '{dotted_path}'")

JK = Engineer("JK", 30, "Master")

print(get_attr("JK.age"))