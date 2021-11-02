# Multiline string with correct indent
# https://stackoverflow.com/a/48112903

import inspect

string = inspect.cleandoc("""
                        line 1
                            * Haha
                            * b

                            * Example: A
                        """)


"""
Expected output:

line 1
    * Haha
    * b

    * Example: A
"""
print(string)