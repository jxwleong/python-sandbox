import unittest

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class TestEmployee(unittest.TestCase):
    def test_Employee_setarr(self):

        Ali = Employee("Ali", "23")

        self.assertEqual("Ali", getattr(Ali, "name"))
        setattr(Ali, "name", "Abu")
        self.assertEqual("Abu", getattr(Ali, "name"))

if __name__ == '__main__':
    unittest.main()