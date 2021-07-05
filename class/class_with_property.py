"""
cliché employee class :P
"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        # _age to prevent circular call
        # https://stackoverflow.com/questions/51341576/variables-starting-with-underscore-for-property-decorator
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 18 or value > 100:
            raise ValueError("You're either too young or too old for this :P")
        self._age = value


AhBeng = Employee("AhBeng", 1)
    