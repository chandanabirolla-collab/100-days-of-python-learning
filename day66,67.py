class Student:

    # Class Variable
    college = "JNTU"

    # Instance Variables
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# Objects
student1 = Student("Chandana", 90)
student2 = Student("Rahul", 85)


# Student 1
print(student1.name)
print(student1.marks)
print(student1.college)

# Student 2
print(student2.name)
print(student2.marks)
print(student2.college)