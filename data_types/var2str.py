import inspect
import unittest

def var2str(var):
    """Convert variable name to string.
    Expect only one reference

    Args:
        var (obj): Variable to convert name to string

    Returns:
        str: String representation of var
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

class Test_var2str(unittest.TestCase):
    def test_var2str(self):
        haha = 123
        self.assertEqual(var2str(haha), "haha")


def get_variable_name(variable):
    """Return variable name in str

    Args:
        variable (any type): Variable which the name will be return

    Returns:
        results [list|str]: Return the name of the variable in
                                * list if more than one variable with same value
                                * str if only one variable with the value
    Reference: https://stackoverflow.com/a/63171710
    """
    results = []
    globalVariables=globals().copy()
    for globalVariable in globalVariables:
        if id(variable) == id(globalVariables[globalVariable]):
            results.append(globalVariable)
    if len(results) == 1: return results[0]
    return results

class Test_get_variable_name(unittest.TestCase):
    def test_get_variable_name_given_one_variable(self):
        global haha
        haha = 123
        self.assertEqual(get_variable_name(haha), "haha")

    def test_get_variable_name_given_two_variable(self):
        global haha
        global lol
        haha = 123
        lol = 123
        self.assertEqual(get_variable_name(haha), ["haha", "lol"])


if __name__ == '__main__':
    unittest.main()