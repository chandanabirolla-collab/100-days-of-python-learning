# 1. Create your custom error name
class CapitalError(Exception):
    pass  # Keeps Python happy while leaving the class empty


# 2. Set the word
word = "quize"
print("Checking the word now...")

# 3. Stop the program with an error if it's not "QUIZE"
if word != "QUIZE":
    raise CapitalError("Please write QUIZE in capital letters!")