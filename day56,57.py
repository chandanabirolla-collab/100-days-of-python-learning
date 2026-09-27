#intro to OOPS
#Classes and Objects

class Student:
    name = "Chandana"
    age = 20

    def study(self):
        print("Student is studying")


# Creating an object
student1 = Student()

# Accessing attributes
print(student1.name)
print(student1.age)

# Calling method
student1.study()