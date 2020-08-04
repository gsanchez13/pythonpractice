# INTEGERS AND FLOATS
x = 15
# right side happens first and left side happens next
# stored in memory to the variable
price = 9.99
# integers are whole numbers and floats are numbers with a floating/decimal point
discount = 0.2
result = price * (1 - discount)
# follows PEMDAS
# functions perform actions or calculate options
# print(result)

# STRINGS
# name = "Rolf"
# print(name)
# print(name * 2)
# Will concatinate the stirngs based on the number of times you want it to appear. Strings can be multiplied in python
a = 25
b = a
b = 17
# same variable being reassigned
# print(a)
# print(b)
# mutability in the languages will allow you to change the original ariable (a) using another variable (b)

# ACTIVITY
var1 = 5
var2 = 5
num1 = 8
num2 = 2
total = num1 * num2

# F-STRINGS IN PYTHON
name = "bob"
greeting = f"Hello, {name}"
# f-strings allow you to embed variables inside strings. Does not change dynamically.
name = "rolf"
# print(greeting)

# TEMPLATE STRINGS WITH .format()
name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
# allows you to define a template that you can reuse will multiple values .
longer_phrase = "Hello {}, today is {}"
formatted = longer_phrase.format("giselle", "Sunday")
# print(formatted)

# USER INPUTS
# username = input("Enter your name: ")
# print(username)
# size_input = input("How tall are you (cm)?: ")
# height_cm = int(size_input)
# height_us = height_cm / 30.48
# print(f"You are {height_us:.2f}")
# formatting syntax allows you to use the f to set a certain amount of variables

# ACTIVITY
# user_age = int(input("Enter your age: "))
# seconds = user_age * 86400
# print(f'Your age : {user_age} is equal to {seconds} seconds')

l = ["Giselle", "Oliver", "Nala", "Sam"]
# defines a list. Lists can have elements added or removed. keeps order. Has attribute 'append' to add items to the end, 'remove' while defining what is to be removed
t = ("Giselle", "Oliver", "Nala")
# defines a tuple. Touples are immutable and cannot be modifed. keeps order. in order to have tuple with single element, comma must be added to the end of element.does not require parenthesis if stating single element in tuple but does require comma
s = {"Giselle", "Oliver", "Nala"}
# defines a set. cannot have duplicate elements. Can have elements added or removed.
# subscript notation works for lists and touples. it can be used in lists to reassign values. has 'add'
# print('l', l[1], 't', t[2])
l[0] = 'Saul'
l.append('Tiffany')
l.remove('Sam')
# print(l)
s.add("Sam")
s.add("Sam")

# SET OPERATIONS ACTIVITY WITH ATTRIBUTES
# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}
# local_friends = friends.difference(abroad)
# .difference takes in inital set and another set and remove from it the second set
# print(local_friends)
# notation for an empty set is set()
local = {"Rolf", "Bob"}
abroad = {"Anne"}
friends = local.union(abroad)
# print(friends)
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
# print(both) 
# intersection finds common elements between both sets

# BOOLEANS
# print(5 == 5)
# single equal sign is for assignment, double is for comparison
# # print( 5 > 5)
# print( 10 != 10)
# Comparisons: ==, != , > , <, >= , <= , is
# is compares if they are the same thing / object

first_list = [1, 2, 3]
second_list = [1, 2, 3]
true_bool = first_list == second_list
false_bool = first_list is second_list
# print(true_bool, false_bool)

# IF STATEMENTS

# day_of_week = input("What day of the week is it today? ").lower()
# day_of_week == 'Sunday'
# print(day_of_week == "Sunday")
# if day_of_week == "sunday":
#     print("Have a great start to your week")
# elif day_of_week == 'monday':
#     print("It is Monday")
# else:
#     print('Full speed ahead')
# if, elif (else if) and else statements used for conditionals.
# indentations are extremely important and tell python which lines of code to run. do not forget to be consistent (4 spaces is the norm)

# 'IN' KEYWORD IN PYTHON AND LOOPS

friends = ["Rolf", "Bob", "Jen"]
# print("Jen" in friends)
movies_watched = {"The Matrix", "Green Book", 'Her'}
# user_movie = input("Enter something you've watched recently: ")
# print(user_movie in movies_watched)

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't seen that one yet!")

number = 7

# while true creates an infinite loop
# while True:
#     user_input = input('Enter y if you would like to play: (Y/n) ')

#     if user_input == "n":
#         break
#     # break here allows you to terminate the loop
#     user_number = int(input('Guess a number: '))
#     if(user_number == number):
#         print("You guessed correctly!")
#     elif number - user_number in (1, -1):
#         print("You were off by one.")
#     else:
#         print("Sorry that's wrong!")
# else:
#     print("Maybe next time")

#FOR LOOP

friends = ['Rolf', 'Jen', 'Bob', 'Anne']

# define a variable that will take the first and future value of this list. good for each element of the list, tuple or set.
# for friend in friends:
#     print(f"{friend} is my friend.")

# for friend in range(4):
#     print(f"{friend} is my friend.")
# allows you to repeat over a list of numbers and returns their index

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)
# sum is the function that returens the aggregate of all numbers in listt and len returns the length of that list

# for grade in grades:
#     total += grade

# print(total / amount)

# LIST COMPREHENSIONS

numbers = [1, 3, 5]
doubled = [n * 2 for n in numbers]
# putting the loop inside the list brackets returns a new list with the iteration and appending
# keep them short since they are one-liners

friends = ['Rolf', 'Jen', 'Bob', 'Anne', 'Sam', 'Samantha', 'Saul']
# conditional in list comprehension. you are generating a new list with list comprehension
starts_s = [friend for friend in friends if friend.startswith('S')]

# for friend in friends:
#     if friend.startswith('S'):
#         starts_s.append(friend)

# print(starts_s)