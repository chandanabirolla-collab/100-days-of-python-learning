#list methods
l=[8,7,6,5,4,3,2,1]
l.append(10)
print(l)
o=[4,7,9,2,3,7]
o.sort()
print(o)
o.sort(reverse=True)
print(o)
fruits = ["apple", "banana", "cherry"]

fruits.append("date")
print("After append:", fruits)
# insert() - Adds an item at a specific index
fruits.insert(1, "orange")
print("After insert:", fruits)
#remove() - Removes an item by its name
fruits.remove("banana")
print("After remove:", fruits)
# pop() - Removes the last item from the list
fruits.pop()
print("After pop:", fruits)
#  sort() - Sorts the list alphabetically
fruits.sort()
print("After sort:", fruits)
#  reverse() - Flips the whole list upside down
fruits.reverse()
print("After reverse:", fruits)
numbers = [1, 2, 3, 4, 5]
print("--- COMPREHENSION ---")

# Multiply every item in the numbers list by 10
ordered_nums = [x * 10 for x in numbers]

print("Original numbers:", numbers)
print("New multiplied list:", ordered_nums)