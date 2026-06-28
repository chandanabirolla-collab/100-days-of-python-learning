from datetime import datetime

# 1. Get the current time and extract the hour
current_hour = datetime.now().hour

# 2. Use if-elif-else to determine the right greeting
if current_hour < 12:
    print("Good morning, sir!")
elif current_hour < 18:
    print("Good afternoon, sir!")
else:
    print("Good evening, sir!")