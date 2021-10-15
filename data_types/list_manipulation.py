import os
import unittest
import xml.etree.ElementTree 
import itertools


def convert_list_to_str(list):
    str_ = ''.join(str(number) for number in list)
    return str_

def is_nested_list(list_):
    return any(isinstance(element, list) for element in list_)


class Test_is_nested_list(unittest.TestCase):
    def test_is_nested_list_given_not_nestedlist__expect_false(self):
        self.assertEqual(False, is_nested_list([1, 2]))
        self.assertEqual(False, is_nested_list(['abc', '!@#$', '11aD']))

    def test_is_nested_list_given_nested_list_expect_true(self):
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4]]))
        self.assertEqual(True, is_nested_list([[1, 2], [3, 4, 'a', '!'], ['AD']]))


def duplicate_list_in_order(list_, n=2):
    if is_nested_list(list_):
        return list(itertools.chain.from_iterable(itertools.repeat(e, n) for e in list_))
    return append_self_if_single_list(list_)


def append_self_if_single_list(list_):
    if is_nested_list(list_) is False:
        temp_list = list_.copy()
        list_= [list_] # Create a nested list for append
        list_.append(temp_list)
        return list_


class Test_duplicate_list_in_order(unittest.TestCase):
    def test_duplicate_list_in_order(self):
        self.assertEqual([[1, 2], [1, 2]], duplicate_list_in_order([1, 2]))
        self.assertEqual([['a', 'b'], ['a', 'b']], duplicate_list_in_order(['a', 'b']))
        self.assertEqual([[1, 2], [1, 2], [3, 4], [3, 4]], duplicate_list_in_order([[1, 2], [3, 4]]))
        self.assertEqual([['low', 'med'], ['low', 'med'], ['3sec', '4sec'], ['3sec', '4sec']], \
                          duplicate_list_in_order([['low', 'med'], ['3sec', '4sec']]))


def setup_list_for_combination(number_lists, include_self):
    if include_self is True:
        number_lists = duplicate_list_in_order(number_lists)
    return number_lists


class Test_setup_list_for_combination(unittest.TestCase):
    def test_setup_list_for_combination_include_self_True(self):
        self.assertEqual([['a', 'b'], ['a', 'b'],['c', 'd'],['c', 'd']], \
            setup_list_for_combination([['a', 'b'], ['c', 'd']], include_self=True))
    
    def test_setup_list_for_combination_include_self_False(self):
        self.assertEqual([['a', 'b'], ['c', 'd']], setup_list_for_combination([['a', 'b'], ['c', 'd']],\
                                                                              include_self=False))


def get_combination_in_list(number_lists, include_self=True): 
    number_lists = list(number_lists)
    number_lists = setup_list_for_combination(number_lists, include_self=include_self)
    combination_list = []
    for item in list(itertools.product(*number_lists)):
        combination_list.append(list(item))
    return combination_list


class Test_get_combination_in_list(unittest.TestCase):
    def test_get_combination_in_list_given_single_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([[1, 1], [1, 2], [2, 1], [2, 2]], get_combination_in_list([1, 2]))
        self.assertEqual([['low', 'low'], ['low', 'med'], ['med', 'low'], ['med', 'med']],    \
                        get_combination_in_list(['low', 'med']))
        self.assertEqual([[1, 1], [1, 2], [1, 3],   \
                          [2, 1], [2, 2], [2, 3],   \
                          [3, 1], [3, 2], [3, 3]], get_combination_in_list([1, 2, 3]))   
    
    def test_get_combination_in_list_given_double_list_expect_get_all_the_possible_combination(self):
        self.assertEqual([['Low', 'Low'], ['Low', 'Med'], ['Med', 'Low'], ['Med', 'Med']],    \
                        get_combination_in_list(['Low', 'Med']))
        self.assertEqual([['3sec', '3sec', 'Low', 'Low'], ['3sec', '3sec', 'Low', 'Med'], ['3sec', '3sec', 'Med', 'Low'], ['3sec', '3sec', 'Med', 'Med'],  \
                          ['3sec', '1sec', 'Low', 'Low'], ['3sec', '1sec', 'Low', 'Med'], ['3sec', '1sec', 'Med', 'Low'], ['3sec', '1sec', 'Med', 'Med'], \
                          ['1sec', '3sec', 'Low', 'Low'], ['1sec', '3sec', 'Low', 'Med'], ['1sec', '3sec', 'Med', 'Low'], ['1sec', '3sec', 'Med', 'Med'], \
                          ['1sec', '1sec', 'Low', 'Low'], ['1sec', '1sec', 'Low', 'Med'], ['1sec', '1sec', 'Med', 'Low'], ['1sec', '1sec', 'Med', 'Med']], \
                          get_combination_in_list([['3sec', '1sec'], ['Low', 'Med']]))
    
    def test_get_combination_in_list_given_double_list_not_include_self_expect_get_all_the_possible_combination(self):    
        self.assertEqual([['Low', '1'], ['Low', '2'], ['Med', '1'], ['Med', '2']],  \
                        get_combination_in_list([['Low', 'Med'],['1','2']], include_self=False))


def convert_args_list_to_nested_list(*args_list):
    args_list = list(args_list)
    nested_list = []

    for list_ in args_list:
        if is_nested_list(list_):
            for element_list in list_:
                nested_list.append(element_list)
        else:        
            nested_list.append(list_)
    return nested_list

class Test_convert_args_list_to_nested_list(unittest.TestCase):
    def test_convert_args_list_to_nested_list_given_n_args_list_expect_convert_to_nested_list(self):
        self.assertEqual([[1, 2], [3, 4]], convert_args_list_to_nested_list([1, 2], [3, 4]))
        self.assertEqual([['Low', 'Med'], ['3sec'], ['Hi']], 
                         convert_args_list_to_nested_list(['Low', 'Med'], ['3sec'], ['Hi']))

    def test_convert_args_list_to_nested_list_given_n_args_list_with_nested_list_expect_convert_to_nested_list(self):
        self.assertEqual([[1, 2], [3, 4], ['a', 'b']], \
                        convert_args_list_to_nested_list([[1, 2], [3, 4]], ['a', 'b']))
        self.assertEqual([['Low', 'Med'], ['3sec'], ['Hi']], 
                         convert_args_list_to_nested_list(['Low', 'Med'], [['3sec'], ['Hi']]))
        self.assertEqual([['Low', 'Med'], ['Hehe'], ['X'], ['NANI'], ['Haha']], 
                         convert_args_list_to_nested_list(['Low', 'Med'], [['Hehe'], ['X']], [['NANI'], ['Haha']]))



def convert_nested_list_element_to_str(list_):
    converted_list = []
    if is_nested_list(list_):
        for element_list in list_:
            element_str = convert_list_to_str(element_list)
            converted_list.append(element_str)
        return converted_list
    return False


class Test_convert_nested_list_element_to_str(unittest.TestCase):
    def test_convert_nested_list_element_to_str(self):
        self.assertEqual(['[1,2]', '[3,4]'], convert_nested_list_element_to_str([[1, 2], [3, 4]]))
        self.assertEqual(['[Hello,World]', '[Hi,There]'], convert_nested_list_element_to_str([['Hello', 'World'], ['Hi', 'There']]))
        self.assertEqual(['[Hello,World]', '[Hi,There]', '[He,he]'], convert_nested_list_element_to_str([['Hello', 'World'], ['Hi', 'There'], ['He', 'he']]))
        self.assertEqual(['[Low]', '[High,Low]'], convert_nested_list_element_to_str([['Low'], ['High', 'Low']]))
        self.assertEqual(False, convert_nested_list_element_to_str(['low', 'high']))


def convert_list_to_str(list_):
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


class Test_convert_list_to_str(unittest.TestCase):
    def test_convert_list_to_str(self):
        self.assertEqual('[1]', convert_list_to_str([1]))
        self.assertEqual('[1,2]', convert_list_to_str([1, 2]))
        self.assertEqual('[Hello,World]', convert_list_to_str(['Hello', 'World']))
        self.assertEqual('[low,high]', convert_list_to_str(['low', 'high']))
        self.assertEqual('[1,2,3,4]', convert_list_to_str([1, 2, 3, 4]))   


def duplicate_list(list_, n=1):
    if isinstance(list_, list) is False:
        raise TypeError("Expecting list but receiving {}".format(type(list_)))
    
    nested_list = [list_]
    while n != 0:
        nested_list.append(list_)
        n -= 1
    return nested_list

class Test_duplicate_list(unittest.TestCase):
    def test_duplicate_list(self):
        self.assertEqual([[1], [1]], duplicate_list([1]))
        self.assertEqual([[1, 2], [1, 2]], duplicate_list([1, 2]))
        self.assertEqual([[1, 2], [1, 2], [1, 2]], duplicate_list([1, 2], 2))
        self.assertEqual([[1, 2], [1, 2], [1, 2], [1, 2]], duplicate_list([1, 2], 3))


def number_to_list_of_integer(num):
    # Ref: https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
    return [int(x) for x in str(num)]


class Test_number_to_list_of_integer(unittest.TestCase):
    def test_number_to_list_of_integer(self):
        self.assertEqual([1, 2, 3], number_to_list_of_integer(123))


def number_to_list_of_ascending_integer(num, start_number=0):
    list_ = []
    for x in range(start_number, num + start_number):
        list_.append(x)
    return list_

class Test_number_to_list_of_ascending_integer(unittest.TestCase):
    def test_number_to_list_of_ascending_integer_start_number_0(self):
        # default start_number=0
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], number_to_list_of_ascending_integer(10))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], number_to_list_of_ascending_integer(10, start_number=0))

    def test_number_to_list_of_ascending_integer_start_number_1(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], number_to_list_of_ascending_integer(10, start_number=1))

if __name__ == '__main__':
    unittest.main()