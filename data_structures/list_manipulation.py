import os
import unittest
import itertools


def append_self_if_singlelist_(*numberlist_s):
    # *numberlist_s is tuple, convert to list because
    # tuple is immutable
    numberlist_s = list(numberlist_s)
    if len(numberlist_s) == 1:
        numberlist_s.append(numberlist_s[0])
    return numberlist_s


def get_combination_inlist_(*numberlist_s): 
    numberlist_s = append_self_if_singlelist_(*numberlist_s)
    combinationlist_ = []
    for item in list(itertools.product(*numberlist_s)):
        combinationlist_.append(list(item))
    return combinationlist_

# def list_to_string(*numberlist_s):
#     strlist_ = []
#     _str = ' '
#     for element in list(numberlist_s):
#         print(str(element))
#         _str.join(str(element))
#
#     strlist_.append(_str)
#     return strlist_

def is_nestedlist_(list_):
    return any(isinstance(element, list) for element in list_)


class Test_is_nestedlist_(unittest.TestCase):
    def test_is_nestedlist__given_not_nestedlist__expect_false(self):
        self.assertEqual(False, is_nestedlist_([1, 2]))
        self.assertEqual(False, is_nestedlist_(['abc', '!@#$', '11aD']))

    def test_is_nestedlist__given_nestedlist__expect_true(self):
        self.assertEqual(True, is_nestedlist_([[1, 2], [3, 4]]))
        self.assertEqual(True, is_nestedlist_([[1, 2], [3, 4, 'a', '!'], ['AD']]))


def convert_nestedlist__element_to_string(list_):
    convertedlist_ = []
    if is_nestedlist_(list_):
        for elementlist_ in list_:
            element_str = convertlist__to_string(elementlist_)
            convertedlist_.append(element_str)
        return convertedlist_
    return False


class Test_convert_nestedlist__element_to_string(unittest.TestCase):
    def test_convert_nestedlist__element_to_string(self):
        self.assertEqual(['[1,2]', '[3,4]'], convert_nestedlist__element_to_string([[1, 2], [3, 4]]))
        self.assertEqual(['[Hello,World]', '[Hi,There]'], convert_nestedlist__element_to_string([['Hello', 'World'], ['Hi', 'There']]))
        self.assertEqual(['[Hello,World]', '[Hi,There]', '[He,he]'], convert_nestedlist__element_to_string([['Hello', 'World'], ['Hi', 'There'], ['He', 'he']]))
        self.assertEqual(['[Low]', '[High,Low]'], convert_nestedlist__element_to_string([['Low'], ['High', 'Low']]))
        self.assertEqual(False, convert_nestedlist__element_to_string(['low', 'high']))


def convertlist__to_string(list_):
    _str = ''
    LAST_INDEX = len(list_) - 1
    for index, element in enumerate(list_):
        if index == 0:
            # If not the only the element don't join the ']', else join ']' to close the list str
            _str = ''.join([_str, '[' + str(element)]) if len(list_) != 1 else ''.join([_str, '[' + str(element) + ']'])
        elif index == LAST_INDEX:
            _str = ''.join([_str, ',' + str(element) + ']'])
        else:
            _str = ''.join([_str, ',' + str(element)])
    return _str


class Test_convertlist__to_string(unittest.TestCase):
    def test_convertlist__to_string(self):
        self.assertEqual('[1]', convertlist__to_string([1]))
        self.assertEqual('[1,2]', convertlist__to_string([1, 2]))
        self.assertEqual('[Hello,World]', convertlist__to_string(['Hello', 'World']))
        self.assertEqual('[low,high]', convertlist__to_string(['low', 'high']))


class Test_append_self_if_singlelist_(unittest.TestCase):
    def test_append_self_if_singlelist__given_singlelist__expect_duplicate_element_oflist_(self):
        self.assertEqual([[1], [1]], append_self_if_singlelist_([1]))
        self.assertEqual([[1, 2], [1, 2]], append_self_if_singlelist_([1, 2]))
        self.assertEqual([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], append_self_if_singlelist_([1, 2, 3, 4, 5]))
        self.assertEqual(['abcd'], ['abcd'], append_self_if_singlelist_(['abcd']))
        self.assertEqual(['aaa', 'sss', 'ddd', 1], ['aaa', 'sss', 'ddd', 1], append_self_if_singlelist_(['aaa', 'sss', 'ddd', 1]))

    def test_append_self_if_singlelist__given_non_singlelist__expect_no_effect(self):
        self.assertEqual([[1], [2]], append_self_if_singlelist_([1], [2]))
        self.assertEqual([[1, 2], [3, 4]], append_self_if_singlelist_([1, 2], [3, 4]))
        self.assertEqual([[1, 2, 3, 4, 5], ['a', 'b']], append_self_if_singlelist_([1, 2, 3, 4, 5], ['a', 'b']))
        self.assertEqual([['abcd'], ['!@#$']], append_self_if_singlelist_(['abcd'], ['!@#$']))
        self.assertEqual([['aaa', 'sss'], [2, 3], [1]], append_self_if_singlelist_(['aaa', 'sss'], [2, 3], [1]))


class Test_get_combination_inlist__inlist_(unittest.TestCase):
    def test_get_combination_inlist__inlist__given_singlelist__expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 1], [1, 2], [2, 1], [2, 2]], get_combination_inlist_([1, 2]))
        self.assertEqual([[1, 1], [1, 2], [1, 3],   \
                          [2, 1], [2, 2], [2, 3],   \
                          [3, 1], [3, 2], [3, 3]], get_combination_inlist_([1, 2, 3]))

    def test_get_combination_inlist__inlist__given_twolist__expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3], [1, 4], [2, 3], [2, 4]], get_combination_inlist_([1, 2], [3, 4]))
        self.assertEqual([[1, 4], [1, 5], [1, 6],   \
                          [2, 4], [2, 5], [2, 6],   \
                          [3, 4], [3, 5], [3, 6]], get_combination_inlist_([1, 2, 3], [4, 5, 6]))

    def test_get_combination_inlist__inlist__given_threelist__expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6],   \
                          [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]], get_combination_inlist_([1, 2], [3, 4], [5, 6]))

    def test_get_combination_inlist__inlist__given_fourlist__expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 6, 7], [1, 3, 6, 8],    \
                          [1, 4, 5, 7], [1, 4, 5, 8], [1, 4, 6, 7], [1, 4, 6, 8],    \
                          [2, 3, 5, 7], [2, 3, 5, 8], [2, 3, 6, 7], [2, 3, 6, 8],    \
                          [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 6, 7], [2, 4, 6, 8]], get_combination_inlist_([1, 2], [3, 4], [5, 6], [7, 8]))


if __name__ == '__main__':
    unittest.main()


