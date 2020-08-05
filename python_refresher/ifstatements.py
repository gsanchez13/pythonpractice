# IF STATEMENTS

day_of_week = input("What day of the week is it today? ").lower()
day_of_week == 'Sunday'
print(day_of_week == "Sunday")
if day_of_week == "sunday":
    print("Have a great start to your week")
elif day_of_week == 'monday':
    print("It is Monday")
else:
    print('Full speed ahead')
# if, elif (else if) and else statements used for conditionals.
# indentations are extremely important and tell python which lines of code to run. do not forget to be consistent (4 spaces is the norm)