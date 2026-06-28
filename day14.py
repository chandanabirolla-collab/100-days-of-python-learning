# Change this value to test different outcomes
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This will run because 85 is >= 80
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
   # nested if
   # Change these to see how the inner logic branches
has_ticket = True
age = 16

if has_ticket:
    print("Welcome to the theater!")
    
    # Outer condition passed; now checking the nested condition
    if age >= 18:
        print("You can watch R-rated movies.")
    else:
        print("You can only watch PG-13 or lower movies.")
        
else:
    print("Please buy a ticket at the front desk first.")