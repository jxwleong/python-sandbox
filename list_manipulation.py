import os
import unittest
import itertools


def append_self_if_single_list(*number_lists):
    # *number_lists is tuple, convert to list because
    # tuple is immutable
    number_lists = list(number_lists)
    if len(number_lists) == 1:
        number_lists.append(number_lists[0])
    return number_lists


def get_combination_in_list(*number_lists): 
    number_lists = append_self_if_single_list(*number_lists)
    combination_list = []
    for item in list(itertools.product(*number_lists)):
        combination_list.append(list(item))
    return combination_list

# def list_to_string(*number_lists):
#     str_list = []
#     _str = ' '
#     for element in list(number_lists):
#         print(str(element))
#         _str.join(str(element))
#
#     str_list.append(_str)
#     return str_list

def is_nested_list(_list):
    return any(isinstance(element, list) for element in _list)


class Test_is_nested_list(unittest.TestCase):
    def test_is_nested_list_given_not_nested_list_expect_false(self):
        self.assertEqual(False, is_nested_list([1, 2]))
        self.assertEqual(False, is_nested_list(['abc', '!@#$', '11aD']))

    def test_is_nested_list_given_nested_list_expect_true(self):
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4]]))
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4, 'a', '!'], ['AD']]))

def list_to_string(*number_lists):
    #number_lists = list(number_lists)
    if is_nested_list(number_lists):
        for index, element in enumerate(number_lists):
            _str = ''
            _str = _str.join('[' + ','.join(number_lists[index]) + ']')    
    elif len(number_lists) == 1:
        return '[' + ','.join(number_lists[0]) + ']'

    else:
        str_list = []
        for element in list(number_lists):
            str_list = '[' + ','.join(element) + ']'
            return str_list

# [[1, 2], [3, 4]] => ["[1, 2]", "[3, 4]"]
#_list = [['low', 'med'], ['3sec', ['1sec']]]
_list = ['low','high']
_str = '[' + ','.join(_list) + ']'
print(_str)
#print(list_to_string(_list))
#print(list_to_string([['low', 'high'], ['3sec', '2sec']]))
_list = [['low', 'high'], ['3sec', '2sec']]


class Test_append_self_if_single_list(unittest.TestCase):
    def test_append_self_if_single_list_given_single_list_expect_duplicate_element_of_list(self):
        self.assertEqual([[1], [1]], append_self_if_single_list([1]))
        self.assertEqual([[1, 2], [1, 2]], append_self_if_single_list([1, 2]))
        self.assertEqual([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], append_self_if_single_list([1, 2, 3, 4, 5]))
        self.assertEqual(['abcd'], ['abcd'], append_self_if_single_list(['abcd']))
        self.assertEqual(['aaa', 'sss', 'ddd', 1], ['aaa', 'sss', 'ddd', 1], append_self_if_single_list(['aaa', 'sss', 'ddd', 1]))

    def test_append_self_if_single_list_given_non_single_list_expect_no_effect(self):
        self.assertEqual([[1], [2]], append_self_if_single_list([1], [2]))
        self.assertEqual([[1, 2], [3, 4]], append_self_if_single_list([1, 2], [3, 4]))
        self.assertEqual([[1, 2, 3, 4, 5], ['a', 'b']], append_self_if_single_list([1, 2, 3, 4, 5], ['a', 'b']))
        self.assertEqual([['abcd'], ['!@#$']], append_self_if_single_list(['abcd'], ['!@#$']))
        self.assertEqual([['aaa', 'sss'], [2, 3], [1]], append_self_if_single_list(['aaa', 'sss'], [2, 3], [1]))


class Test_get_combination_in_list_in_list(unittest.TestCase):
    def test_get_combination_in_list_in_list_given_single_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 1], [1, 2], [2, 1], [2, 2]], get_combination_in_list([1, 2]))
        self.assertEqual([[1, 1], [1, 2], [1, 3],   \
                          [2, 1], [2, 2], [2, 3],   \
                          [3, 1], [3, 2], [3, 3]], get_combination_in_list([1, 2, 3]))

    def test_get_combination_in_list_in_list_given_two_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3], [1, 4], [2, 3], [2, 4]], get_combination_in_list([1, 2], [3, 4]))
        self.assertEqual([[1, 4], [1, 5], [1, 6],   \
                          [2, 4], [2, 5], [2, 6],   \
                          [3, 4], [3, 5], [3, 6]], get_combination_in_list([1, 2, 3], [4, 5, 6]))

    def test_get_combination_in_list_in_list_given_three_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6],   \
                          [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]], get_combination_in_list([1, 2], [3, 4], [5, 6]))

    def test_get_combination_in_list_in_list_given_four_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 6, 7], [1, 3, 6, 8],    \
                          [1, 4, 5, 7], [1, 4, 5, 8], [1, 4, 6, 7], [1, 4, 6, 8],    \
                          [2, 3, 5, 7], [2, 3, 5, 8], [2, 3, 6, 7], [2, 3, 6, 8],    \
                          [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 6, 7], [2, 4, 6, 8]], get_combination_in_list([1, 2], [3, 4], [5, 6], [7, 8]))


if __name__ == '__main__':
    unittest.main()


