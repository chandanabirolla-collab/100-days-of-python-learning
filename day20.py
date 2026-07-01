#do while
while True:
    # 1. Your code runs here automatically
    secret_code = input("Enter password: ")
    
    # 2. Condition is checked at the bottom
    if secret_code == "1234":
        print("Access Granted!")
        break  # 3. Breaks the loop if correct
        
    print("Wrong! Try again.")

    #functions
    # 1. Define the function
def greet_user(name):
    print("hello " + name +" , welcome back!")

# 2. Call the function (this is how you use it)
greet_user("Bro")
greet_user("Alex")

# Define a function to square a number
def square_number(number):
    return  number * number

# Call the function and store the result in a variable
result = square_number(5)

print("The square of 5 is:",result)
# Output: The square of 5 is: 25