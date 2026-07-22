# set methods
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
fruits.update(["mango", "grape"])
print(fruits)
fruits.remove("banana")
fruits.discard("pineapple")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))
print("Symmetric Diff:", set_a.symmetric_difference(set_b))
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection_update(b))
x = {10, 20, 30}
y = {20, 40}
(x.difference_update(y))
print(x)
s1 = {1, 2}
s2 = {1, 2, 3, 4}
s3 = {5, 6}
print("Is s1 subset of s2?:", s1.issubset(s2))
print("Is s2 superset of s1?:", s2.issuperset(s1)) 
print("Are s1 and s3 disjoint?:", s1.isdisjoint(s3))