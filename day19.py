#break and continue statements
# A list of items in a box
box = ["book", "pencil", "key", "wallet", "headphones"]

for item in box:
    print(item)
    
    if item == "key":
        print("-> Found the key! Stopping the search.")
        break  # This instantly exits the loop

print("Loop closed.")
#continue
for num in range(1, 6):  # Generates numbers 1, 2, 3, 4, 5
    if num == 3:
        print("Skipping 3!")
        continue  # Jumps straight back to the top of the loop for number 4
        
    print(num)
while True:
    
    secret_code = input("Enter password: ")
    
    #  Condition is checked at the bottom
    if secret_code == "1234":
        print("Access Granted!")
        break  #  Breaks the loop if correct
        
    print("Wrong! Try again.")