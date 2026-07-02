print("****wellcome to candys quize game****")
print("answer using A,B,C,D")
#list of questions 
questions=[
    "Who is the current Prime Minister of India?",
    "Who is the current Minister of Finance of India?",
    "If 3 cats can catch 3 mice in 3 minutes, how many minutes does it take for 100 cats to catch 100 mice?",
    "Complete the logical series: 2, 6, 12, 20, 30, ?",
    "In which city is the famous 'Charminar' monument located?",
]
#list of options
options=[
    ["A. Rahul Gandhi", "B. Amit Shah", "C. Narendra Modi", "D. Rajnath Singh"],
    ["A. Smriti Irani", "B. Nirmala Sitharaman", "C. Piyush Goyal", "D. Ashwini Vaishnaw"],
    ["A. 100 minutes", "B. 30 minutes", "C. 3 minutes", "D. 1 minute"],
    ["A. 40", "B. 42", "C. 44", "D. 46"],
    ["A. Mumbai", "B. Hyderabad", "C. Delhi", "D. Bengaluru"],
]
#list of correct answers 
correctanswers=["C","B","C","B","B"]
# 4. A list of cash prizes
prizes = [1000, 5000, 10000, 50000, 100000]
# This variable tracks the total money won
current_money = 0
#loop
for i in range(5):
    print("QUESTION for Rs", prizes[i], ":")
    print(questions[i])
    # Print the 4 options for this question
    for opt in options[i]:
     print(opt)
 # Get user answer
    user_answer = input("Your answer: ").upper()
    # Check if the answer matches our correct answers list
    if user_answer == correctanswers[i]:
        current_money = prizes[i]
        print(" Correct! You have won Rs", current_money)
        print() # This just leaves an empty line for neatness
    else:
        print("Wrong! Game Over.")
        print("You go home with Rs", current_money)
        break # This breaks the loop and stops the game
    # This goes outside the loop at the very end of your file
print(" Congratulations bro! You finished the game and won Rs", current_money)