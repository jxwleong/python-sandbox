import unittest
from unittest.runner import TextTestResult

def remove_space(str_):
    if isinstance(str_, str):
        return str_.replace(' ', '')
    raise TypeError("Invalid string argument str_: " + str(str_))


class Test_remove_space(unittest.TestCase):
    def test_remove_space_given_str_with_spaces_expect_spaces_removed(self):
        self.assertEqual('ab', remove_space(' ab'))
        self.assertEqual('XDQ', remove_space('X D Q'))
        self.assertEqual('#@2313W@#!#!@#SADsa', remove_space('# @ 23 13 W @#!#!@# SAD sa'))

    def test_remove_space_given_str_with_no_spaces_expect_no_effect(self):
        self.assertEqual('ab', remove_space('ab'))
        self.assertEqual('HELLOworld!', remove_space('HELLOworld!'))

    def test_remove_space_given_non_str_expect_TypeError_exception_throw(self):
        self.assertRaises(TypeError, remove_space, 999)
        self.assertRaises(TypeError, remove_space, [1, 2])
        self.assertRaises(TypeError, remove_space, {'key': 123})
        self.assertRaises(TypeError, remove_space, ('Hi', 'There'))



def delimited_str_to_list(str, delimiter=",", remove_space=True):
    list_ = []
    try:
        list_ = str.split(delimiter)
    except:
        list_ = [str]

    # Remove space " " elements in list_
    # Ref: https://stackoverflow.com/a/3845449
    if remove_space is True:
        # Needed the element.replace(" ", "") to remove spaces in str element
        list_ = [element.replace(" ", "") for element in list_ if element.strip()]
    return list_


class Test_delimited_str_to_list(unittest.TestCase):
    def test_delimited_str_to_list_given_delimter(self):
        self.assertEqual(["a", "b"], delimited_str_to_list("a   ,b,"))
        self.assertEqual(["haha", "lol"], delimited_str_to_list("haha;lol", delimiter=";"))
        self.assertEqual(["test"," you there?"], delimited_str_to_list("test, you there?",remove_space=False))

    def test_delimited_str_to_list_given_one_str_only(self):
        self.assertEqual(["a"], delimited_str_to_list("a "))
        self.assertEqual(["a"], delimited_str_to_list("a,"))
        self.assertEqual(["a"], delimited_str_to_list("  a,  "))

if __name__ == '__main__':
    unittest.main()