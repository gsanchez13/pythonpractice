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
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)
# .difference takes in inital set and another set and remove from it the second set
# print(local_friends)
# notation for an empty set is set()
local = {"Rolf", "Bob"}
abroad = {"Anne"}
friends = local.union(abroad)
print(friends)
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)
# intersection finds common elements between both sets