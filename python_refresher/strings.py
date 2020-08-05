# STRINGS

name = "Rolf"
print(name)
print(name * 2)
# Will concatinate the stirngs based on the number of times you want it to appear. Strings can be multiplied in python
a = 25
b = a
b = 17
# same variable being reassigned
print(a)
print(b)
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
print(greeting)

# TEMPLATE STRINGS WITH .format()
name = "Bob"
greeting = "Hello, {}"
# with_name = greeting.format(name)
# allows you to define a template that you can reuse will multiple values .
longer_phrase = "Hello {}, today is {}"
formatted = longer_phrase.format("giselle", "Sunday")
print(formatted)
