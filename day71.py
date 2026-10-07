class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("Student is studying")


student = Student("Chandana", 20)

# 1. dir()
print(dir(student))

# 2. __dict__
print(student.__dict__)

# 3. help()
help(student)