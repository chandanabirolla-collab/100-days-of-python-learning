class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Chandana")

print(student)