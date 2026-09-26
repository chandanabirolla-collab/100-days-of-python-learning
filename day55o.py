# Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a draw!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")

else:
    print("Computer wins!")
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

for round in range(1, 4):

    print(f"\n--- Round {round} ---")

    user = input("Enter rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

print("\n--- Final Score ---")
print("Your score:", user_score)
print("Computer score:", computer_score)

if user_score > computer_score:
    print("🎉 You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("🤝 Overall draw!")