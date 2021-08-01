import unittest

class Employee:
    def __init__(self, name, age):
        self.name = name
        # _age to prevent circular call
        # https://stackoverflow.com/questions/51341576/variables-starting-with-underscore-for-property-decorator
        self.age = age

class Engineer(Employee):
    def __init__(self, name, age, qualification):
        super().__init__(name, age)
        self.qualification = qualification

class Test_Class_Engineer(unittest.TestCase):
    def test_class_engineer(self):
        JK = Engineer("JK", 30, "Master")
        self.assertEqual(JK.name, "JK")
        self.assertEqual(JK.age, 30)
        self.assertEqual(JK.qualification, "Master")


if __name__ == '__main__':
    unittest.main()
