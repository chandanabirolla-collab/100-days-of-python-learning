class Student:

    college = "JNTU"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college


# Before changing
print(Student.college)

# Change class variable
Student.change_college("ABC College")

# After changing
print(Student.college)