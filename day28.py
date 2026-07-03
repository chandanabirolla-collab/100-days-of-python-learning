letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Candy"

print(letter.format(name , country))
print(f"Hey my name is {name} and I am from {country}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))