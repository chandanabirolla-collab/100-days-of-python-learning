#Syntax of python constructor
#def __init__(self):
#constuctors Parameterized
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Chandana", 20)

print(student1.name)
print(student1.age)
# Default Constructor
class StudentDefault:
    def __init__(self):
        print("Student created")

student2 = StudentDefault()