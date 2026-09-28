#Access Modifiers

class Student:

    def __init__(self):
        self.name = "Chandana"       # Public
        self._age = 20               # Protected
        self.__marks = 90            # Private


student = Student()

# Public
print(student.name)

# Protected
print(student._age)

# Private
# print(student.__marks)   # This will give an error