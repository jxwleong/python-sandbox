"""
Sandbox for python class
"""

class SandboxClass():
    value = []
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def get_digit(list):
        value = []
        #global value
        for element in list:
            if element.isdigit() is True:
                value.append(element)
        return value


if __name__ == '__main__':
    a = SandboxClass.get_digit(["1", "s", "111"])
    print(a)