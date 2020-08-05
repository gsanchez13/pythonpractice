# USER INPUTS

username = input("Enter your name: ")
print(username)
size_input = input("How tall are you (cm)?: ")
height_cm = int(size_input)
height_us = height_cm / 30.48
print(f"You are {height_us:.2f}")
# formatting syntax allows you to use the f to set a certain amount of variables

# ACTIVITY

user_age = int(input("Enter your age: "))
seconds = user_age * 86400
print(f'Your age : {user_age} is equal to {seconds} seconds')