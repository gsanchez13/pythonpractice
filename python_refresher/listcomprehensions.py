# LIST COMPREHENSIONS

numbers = [1, 3, 5]
doubled = [n * 2 for n in numbers]
# putting the loop inside the list brackets returns a new list with the iteration and appending
# keep them short since they are one-liners

friends = ['Rolf', 'Jen', 'Bob', 'Anne', 'Sam', 'Samantha', 'Saul']
# conditional in list comprehension. you are generating a new list with list comprehension. you can use the function id(<list name>) which will give you the ID of the list stored in memory
starts_s = [friend for friend in friends if friend.startswith('S')]

for friend in friends:
    if friend.startswith('S'):
        starts_s.append(friend)

print(starts_s)