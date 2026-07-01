# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry", "banana", "apple", "banana")

print("The Tuple:", fruits)
print()


# METHOD 1: count()

banana_count = fruits.count("banana")

print("--- 1. COUNT METHOD ---")
print("How many bananas:", banana_count)  # Output: 3
print()


# METHOD 2: index()
cherry_position = fruits.index("cherry")

print("--- 2. INDEX METHOD ---")
print("Index of cherry:", cherry_position)  # Output: 2