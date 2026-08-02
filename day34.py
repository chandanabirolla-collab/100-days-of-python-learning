#dictionary methods 
user = {
    "name": "Alex",
    "role": "Developer"
}
user["location"] = "New York"
user["role"] = "Lead Developer"
user.update(age=67)
print(user)
user.popitem()
print(user)
del user["name"]
print(user)