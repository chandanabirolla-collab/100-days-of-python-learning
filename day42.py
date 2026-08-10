fruits = ["apple", "banana", "mango"]

# enumerate() gives you both the index (number) and the item
for index, fruit in enumerate(fruits):
    print(index, fruit)
tasks = ["Email", "Meeting", "Coding", "Break"]

for index, task in enumerate(tasks):
    if index % 2 == 0:
        print("==")
    else:
        print("task,index")
        tasks = ["Email", "Meeting", "Coding", "Break"]

for index, task in enumerate(tasks):
    if index % 2 == 0:
        print(f"Task {index}: [PRIORITY] {task}")
    else:
        print(f"Task {index}: [NORMAL] {task}")
fruits = ["apple", "banana", "mango"]

# enumerate() gives you both the index (number) and the item
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)