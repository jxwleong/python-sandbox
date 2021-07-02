"""
Sandbox for python class
"""

class SandboxClass():
    value = []

    def get_digit(list):
        value = []
        #global value
        for element in list:
            if element.isdigit() is True:
                value.append(element)
        return value


a = SandboxClass.get_digit(["1", "s", "111"])
print(a)