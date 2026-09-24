

from functools import reduce

# map()
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

# filter()
result = list(filter(lambda x: x > 2, numbers))
print(result)

# reduce()
result = reduce(lambda x, y: x + y, numbers)
print(result)