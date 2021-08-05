# https://www.geeksforgeeks.org/inner-class-in-python/
import unittest

class Employee:
    def __init__(self, type, name, age):
        # _age to prevent circular call
        # https://stackoverflow.com/questions/51341576/variables-starting-with-underscore-for-property-decorator
        if type == "Engineer":
            self.engineer = self.Engineer(name, age, "Master in Electronics")
        else:
            raise Exception(f"Invalid employee type: {type}")

    class Engineer:
        def __init__(self, name, age, qualification):
            self.name = name
            self.age = age
            self.qualification = qualification


class Test_EmployeeClass(unittest.TestCase):
    def test_EmployeeClass_Engineer_expect_object_init_correct(self):
        employee = Employee("Engineer", "JKK", 20)
        self.assertEqual(employee.engineer.name, "JKK")
        self.assertEqual(employee.engineer.age, 20)
        self.assertEqual(employee.engineer.qualification, "Master in Electronics")

    def test_EmployeeClass_Doctor_expect_exception_thrown(self):
       self.assertRaises(Exception, Employee, "Doctor", "JKK", 20)

if __name__ == '__main__':
    unittest.main()