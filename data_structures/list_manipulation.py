import os
import unittest
import itertools


def append_self_if_single_list(list_):
    # *numberlist_s is tuple, convert to list because
    # tuple is immutable
    list_ = list(list_)
    if is_nested_list(list_) is False:
        [list_.append(element) for element in list_]
    return list_


def get_combination_in_list(*list_): 
    list_ = append_self_if_single_list(*list_)
    combination_list = []
    for item in list(itertools.product(*list_)):
        combination_list.append(list(item))
    return combination_list

def list_to_string(*list_):
    str_list = []
    str_ = ' '
    for element in list(list_):
        print(str(element))
        str_.join(str(element))

    str_list.append(str_)
    return str_list

def is_nested_list(list_):
    return any(isinstance(element, list) for element in list_)


class Test_is_nested_list(unittest.TestCase):
    def test_is_nested_list_given_not_nested_list_expect_false(self):
        self.assertEqual(False, is_nested_list([1, 2]))
        self.assertEqual(False, is_nested_list(['abc', '!@#$', '11aD']))

    def test_is_nested_list_given_nested_list_expect_true(self):
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4]]))
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4, 'a', '!'], ['AD']]))


def convert_nested_list_element_to_string(list_):
    converted_list = []
    if is_nested_list(list_):
        for list_element in list_:
            element_str = convert_list_to_string(list_element)
            converted_list.append(element_str)
        return converted_list
    return False


class Test_convert_nested_list_element_to_string(unittest.TestCase):
    def test_convert_nested_list_element_to_string(self):
        self.assertEqual(['[1,2]', '[3,4]'], convert_nested_list_element_to_string([[1, 2], [3, 4]]))
        self.assertEqual(['[Hello,World]', '[Hi,There]'], convert_nested_list_element_to_string([['Hello', 'World'], ['Hi', 'There']]))
        self.assertEqual(['[Hello,World]', '[Hi,There]', '[He,he]'], convert_nested_list_element_to_string([['Hello', 'World'], ['Hi', 'There'], ['He', 'he']]))
        self.assertEqual(['[Low]', '[High,Low]'], convert_nested_list_element_to_string([['Low'], ['High', 'Low']]))
        self.assertEqual(False, convert_nested_list_element_to_string(['low', 'high']))


def convert_list_to_string(list_):
    str_ = ''
    LAST_INDEX = len(list_) - 1
    for index, element in enumerate(list_):
        if index == 0:
            # If not the only the element don't join the ']', else join ']' to close the list str
            str_ = ''.join([str_, '[' + str(element)]) if len(list_) != 1 else ''.join([str_, '[' + str(element) + ']'])
        elif index == LAST_INDEX:
            str_ = ''.join([str_, ',' + str(element) + ']'])
        else:
            str_ = ''.join([str_, ',' + str(element)])
    return str_


class Test_convert_list_to_string(unittest.TestCase):
    def test_convert_list_to_string(self):
        self.assertEqual('[1]', convert_list_to_string([1]))
        self.assertEqual('[1,2]', convert_list_to_string([1, 2]))
        self.assertEqual('[Hello,World]', convert_list_to_string(['Hello', 'World']))
        self.assertEqual('[low,high]', convert_list_to_string(['low', 'high']))


# class Test_append_self_if_single_list(unittest.TestCase):
#     def test_append_self_if_single_list_given_single_list_expect_duplicate_element_of_list(self):
#         self.assertEqual([1, 1], append_self_if_single_list([1]))
#         self.assertEqual([[1, 2], [1, 2]], append_self_if_single_list([1, 2]))
#         self.assertEqual([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], append_self_if_single_list([1, 2, 3, 4, 5]))
#         self.assertEqual(['abcd'], ['abcd'], append_self_if_single_list(['abcd']))
#         self.assertEqual(['aaa', 'sss', 'ddd', 1], ['aaa', 'sss', 'ddd', 1], append_self_if_single_list(['aaa', 'sss', 'ddd', 1]))

#     def test_append_self_if_single_list_given_non_single_list_expect_no_effect(self):
#         self.assertEqual([[1], [2]], append_self_if_single_list([[1], [2]]))
#         self.assertEqual([[1, 2], [3, 4]], append_self_if_single_list([[1, 2], [3, 4]]))
#         self.assertEqual([[1, 2, 3, 4, 5], ['a', 'b']], append_self_if_single_list([[1, 2, 3, 4, 5], ['a', 'b']]))
#         self.assertEqual([['abcd'], ['!@#$']], append_self_if_single_list([['abcd'], ['!@#$']]))
#         self.assertEqual([['aaa', 'sss'], [2, 3], [1]], append_self_if_single_list([['aaa', 'sss'], [2, 3], [1]]))


class Test_get_combination_in_list(unittest.TestCase):
    def test_get_combination_in_list_given_singlelist_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 1], [1, 2], [2, 1], [2, 2]], get_combination_in_list([1, 2]))
        self.assertEqual([[1, 1], [1, 2], [1, 3],   \
                          [2, 1], [2, 2], [2, 3],   \
                          [3, 1], [3, 2], [3, 3]], get_combination_in_list([1, 2, 3]))

#     def test_get_combination_in_list_given_twolist_expect_get_all_the_possible_combination(self):
#         self.assertEqual([[1, 3], [1, 4], [2, 3], [2, 4]], get_combination_in_list([1, 2], [3, 4]))
#         self.assertEqual([[1, 4], [1, 5], [1, 6],   \
#                           [2, 4], [2, 5], [2, 6],   \
#                           [3, 4], [3, 5], [3, 6]], get_combination_in_list([1, 2, 3], [4, 5, 6]))

#     def test_get_combination_in_list_given_threelist__expect_get_all_the_possible_combination(self):
#         self.assertEqual([[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6],   \
#                           [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]], get_combination_in_list([1, 2], [3, 4], [5, 6]))

#     def test_get_combination_in_list_given_fourlist__expect_get_all_the_possible_combination(self):
#         self.assertEqual([[1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 6, 7], [1, 3, 6, 8],    \
#                           [1, 4, 5, 7], [1, 4, 5, 8], [1, 4, 6, 7], [1, 4, 6, 8],    \
#                           [2, 3, 5, 7], [2, 3, 5, 8], [2, 3, 6, 7], [2, 3, 6, 8],    \
#                           [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 6, 7], [2, 4, 6, 8]], get_combination_in_list([1, 2], [3, 4], [5, 6], [7, 8]))


if __name__ == '__main__':
    unittest.main()


