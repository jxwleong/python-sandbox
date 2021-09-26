import unittest

class Person:
    """
    Base Class
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Engineer(Person):
    """
    Derived Class
    """
    def __init__(self, qualification, *args, **kwargs):
        self.qualification = qualification
        super().__init__(*args, **kwargs)


engineer = Engineer("Master", "X", 20)
print(f"Qualification: {engineer.qualification}")
print(f"Name: {engineer.name}")
print(f"Age: {engineer.age}")


class Test_Class_Person(unittest.TestCase):
    def test_instantiate_Person(self):
        person = Person(name="Jay", age=3)
        self.assertEqual(person.name, "Jay")
        self.assertEqual(person.age, 3)

class Test_Class_Person(unittest.TestCase):
    def test_instantiate_Person(self):
        engineer = Engineer("Master of Science", "X", 20)
        self.assertEqual(engineer.qualification, "Master of Science")
        self.assertEqual(engineer.name, "X")
        self.assertEqual(engineer.age, 20)

if __name__ == "__main__":
    unittest.main()