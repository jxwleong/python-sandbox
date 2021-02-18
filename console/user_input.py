import unittest
from unittest.mock import patch

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def user_input(message, debug_mode=False, completer=None):
    if debug_mode:
        return input(message)
    else:
        return prompt(message, completer=completer, complete_while_typing=True)

completer = WordCompleter(['Hello', 'World'])
# text = user_input('Hello Debug: ', debug_mode=True)
# print('You said: %s Debug Mode' % text)

# text = user_input('Hello Prod: ', completer=completer)
# print('You said: %s Debug Prod' % text)

def return_user_input_in_list(n):
    list_ = []

    for _ in range(n):
        list_.append(input('Enter: '))
    return list_

   
class test_user_input(unittest.TestCase):
    @patch('builtins.input', return_value='Hello')
    def test_user_input_with_mock_patch_single_mocked_value(self, mock_input):
        self.assertEqual('Hello', user_input('Hello Debug: ', debug_mode=True))
        self.assertRaises(TypeError, 'Hello', user_input, 'Hello Debug: ', debug_mode=False, completer=completer)

    @patch('builtins.input', side_effect=['Hello', 'World'])
    def test_user_input_with_mock_patch_multiple_mocked_value(self, mock_input):
        self.assertEqual('Hello', user_input('Hello Debug: ', debug_mode=True))
        self.assertEqual('World', user_input('Hello Debug: ', debug_mode=True))

class test_return_user_input_in_list(unittest.TestCase):
    @patch('builtins.input', side_effect=['Hello', 'World'])
    def test_return_user_input_in_list_given_Hello_World_expect_list_with_element_Hello_World(self, mock_input):
        self.assertEqual(['Hello', 'World'], return_user_input_in_list(n=2))


if __name__ == '__main__':
    unittest.main()