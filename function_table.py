"""
Example of using function table using dictionary to call function
"""
import unittest

def equal(x: int, y: int) -> bool:
    """
    return True if x = y
    else return False
    """   
    return x == y

def not_equal(x: int, y: int) -> bool:
    """
    return True if x != y
    else return False
    """   
    return x != y

def less_than(x: int, y: int) -> bool:
    """
    return True if x < y
    else return False
    """
    return x < y

def less_than_or_equal(x: int, y: int) -> bool:
    """
    return True if x <= y
    else return False
    """
    return x <= y

def greater_than(x: int, y: int) -> bool:
    """
    return True if x > y
    else return False
    """
    return x > y  

def greater_than_or_equal(x: int, y: int) -> bool:
    """
    return True if x >= y
    else return False
    """
    return x >= y




function_table = {
    "=": equal,
    "!=": not_equal,
    "<": less_than,
    "<=": less_than_or_equal,
    ">": greater_than,
    ">=": greater_than_or_equal,
}



class Test_function_table(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(True, function_table["="](1, 1))
        self.assertEqual(False, function_table["="](0, 1))
        self.assertEqual(False, function_table["="]("0", 1))

    def test_not_equal(self):
        self.assertEqual(False, function_table["!="](1, 1))
        self.assertEqual(True, function_table["!="](0, 1))
        self.assertEqual(True, function_table["!="]("0", 1))

    def test_less_than(self):
        self.assertEqual(False, function_table["<"](1, 1))
        self.assertEqual(True, function_table["<"](0, 1))
        self.assertRaises(TypeError, function_table["<"], "0", 1)

    def test_less_than_or_equal(self):
        self.assertEqual(True, function_table["<="](1, 1))
        self.assertEqual(True, function_table["<="](0, 1))
        self.assertEqual(False, function_table["<="](3, 1))
        self.assertRaises(TypeError, function_table["<="], "0", 1)

    def test_greater_than(self):
        self.assertEqual(False, function_table[">"](1, 1))
        self.assertEqual(True, function_table[">"](3, 1))
        self.assertRaises(TypeError, function_table[">"], "0", 1)

    def test_greater_than_or_equal(self):
        self.assertEqual(True, function_table[">="](1, 1))
        self.assertEqual(True, function_table[">="](3, 1))
        self.assertEqual(False, function_table[">="](0, 1))
        self.assertRaises(TypeError, function_table[">="], "0", 1)


if __name__ == '__main__':
    unittest.main()   