# https://www.geeksforgeeks.org/inner-class-in-python/
import unittest
import functools

class Employee:
    def __init__(self, type, name, age):
        # _age to prevent circular call
        # https://stackoverflow.com/questions/51341576/variables-starting-with-underscore-for-property-decorator
        if type == "Engineer":
            self.engineer = self.Engineer(name, age, "Master in Electronics")
        else:
            raise Exception(f"Invalid employee type: {type}")

    class Engineer:
        def __init__(self, name, age, qualification):
            self.name = name
            self.age = age
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

class Test_get_attr(unittest.TestCase):
    def test_get_attr(self):
        global employee
        employee = Employee("Engineer", "JKK", 20)
        self.assertEqual(get_attr("employee.engineer.name"), "JKK")
        self.assertEqual(get_attr("employee.engineer.age"), 20)
        self.assertEqual(get_attr("employee.engineer.qualification"), "Master in Electronics")

if __name__ == '__main__':
    unittest.main()