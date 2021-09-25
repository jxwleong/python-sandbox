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