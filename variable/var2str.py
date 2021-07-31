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


if __name__ == '__main__':
    unittest.main()