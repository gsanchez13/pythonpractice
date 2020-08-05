# FOR LOOP

friends = ['Rolf', 'Jen', 'Bob', 'Anne']

# define a variable that will take the first and future value of this list. good for each element of the list, tuple or set.
for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(4):
    print(f"{friend} is my friend.")
# allows you to repeat over a list of numbers and returns their index

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)
# sum is the function that returens the aggregate of all numbers in listt and len returns the length of that list

# for grade in grades:
#     total += grade

print(total / amount)