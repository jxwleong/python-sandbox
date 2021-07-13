import unittest
import sys
import inspect
import os

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class TestEmployee(unittest.TestCase):
    def test_Employee_setarr(self):

        Ali = Employee("Ali", "23")

        self.assertEqual("Ali", getattr(Ali, "name"))
        setattr(Ali, "name", "Abu")
        self.assertEqual("Abu", getattr(Ali, "name"))



def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    from importlib import import_module
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        msg = "%s doesn't look like a module path" % dotted_path
        print(msg)
        #six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError:
        msg = 'Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        #six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])

Ali = Employee("Ali", "23")

def get_attr(dotted_path):
    try:
        class_name, attribute = dotted_path.split('.', 1)
        return getattr(globals()[class_name], attribute)
    except:
        raise Exception(f"Received invalid dotted path '{dotted_path}'")

    obj_type = type(dotted_path)
    print(dotted_path)
    temp_obj = obj_type()
    return "Haha"

def set_attr(dotted_path, value):
    try:
        class_name, attribute = dotted_path.split('.', 1)
        return setattr(globals()[class_name], attribute, value)
    except:
        raise Exception(f"Received invalid dotted path '{dotted_path}'")

print(get_attr("Ali.age"))
print(set_attr("Ali.age", 1))
print(get_attr("Ali.age"))
print(get_attr("Ali.name"))
print(set_attr("Ali.name", "Abu"))
print(get_attr("Ali.name"))
get_attr("Abu.name")
# t = type(Ali)
# temp = t("temp", 2)
# print(temp.age)
# b =inspect.getmodule(Ali)
# print(b)


# b =inspect.getmodule(unittest)
# print(b)

#print(__main__.Employee)
#a = import_string(".age")
#print(a)
if __name__ == '__main__':
    unittest.main()


