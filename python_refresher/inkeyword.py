# 'IN' KEYWORD IN PYTHON AND LOOPS

friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)
movies_watched = {"The Matrix", "Green Book", 'Her'}
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't seen that one yet!")

number = 7

# while true creates an infinite loop
while True:
    user_input = input('Enter y if you would like to play: (Y/n) ')

    if user_input == "n":
        break
    # break here allows you to terminate the loop
    user_number = int(input('Guess a number: '))
    if(user_number == number):
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry that's wrong!")
else:
    print("Maybe next time")
