# BOOLEANS
print(5 == 5)
# single equal sign is for assignment, double is for comparison
print( 5 > 5)
print( 10 != 10)
# Comparisons: ==, != , > , <, >= , <= , is
# is compares if they are the same thing / object

first_list = [1, 2, 3]
second_list = [1, 2, 3]
true_bool = first_list == second_list
false_bool = first_list is second_list
print(true_bool, false_bool)