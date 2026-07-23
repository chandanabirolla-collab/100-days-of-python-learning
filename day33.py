# Creating a dictionary of student grades
student = {
    "name": "Alex",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student)
print(student["name"])
print(student.get("num"))
#update 
student["age"]=33
print(student)
scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
for name in scores.keys():
    print(name)
for name in student.keys():
    print(name)
for key in student.values():
    print(key)