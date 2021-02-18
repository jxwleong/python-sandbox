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

class test_user_input(unittest.TestCase):
    @patch('builtins.input', return_value='Hello')
    def test_user_input_with_mock_patch_single_mocked_value(self, input):
        self.assertEqual('Hello', user_input('Hello Debug: ', debug_mode=True))
        self.assertRaises(TypeError, 'Hello', user_input, 'Hello Debug: ', debug_mode=False, completer=completer)

    @patch('builtins.input', side_effect=['Hello', 'World'])
    def test_user_input_with_mock_patch_multiple_mocked_value(self, mock_input):
        self.assertEqual('Hello', user_input('Hello Debug: ', debug_mode=True))
        self.assertEqual('World', user_input('Hello Debug: ', debug_mode=True))

if __name__ == '__main__':
    unittest.main()