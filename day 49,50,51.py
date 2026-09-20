

# open() and write()
f = open("myfile.txt", "w")
f.write("Hello Python\n")
f.write("I am learning File Handling\n")

# writelines()
lines = ["Day 49\n", "Day 50\n", "Day 51\n"]
f.writelines(lines)

# close()
f.close()


# read()
f = open("myfile.txt", "r")
print(f.read())
# Append
f = open("myfile.txt", "a")
f.write("This is appended text.\n")
f.close()
# seek()
f.seek(0)

# readline()
print(f.readline())

# readlines()
print(f.readlines())

# tell()
print(f.tell())

# close()
f.close()