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
# Comparisons: ==, != , > , <, >= , <=