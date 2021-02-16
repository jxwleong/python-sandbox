from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def user_input(message, debug_mode=False, completer=None):
    if debug_mode:
        return input(message)
    else:
        return prompt(message, completer=completer, complete_while_typing=True)

completer = WordCompleter(['Hello', 'World'])
text = user_input('Hello Debug: ', debug_mode=True)
print('You said: %s Debug Mode' % text)

text = user_input('Hello Prod: ', completer=completer)
print('You said: %s Debug Prod' % text)

