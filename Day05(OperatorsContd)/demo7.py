# Membership operator:(Relational operators)
# Also works on iterables (list, tuple, set, dict)

# There are 2 types: in , not in

list1 = ['Archana','Bhavana','Preethi','Rama','Seetha']

# in - Returns True if an item is present(is a member) in the iterable
print('Archana' in list1)
# True

print('Krishna' in list1)
# False

list2 = [10,20,30,40,50,60]
print(30 in list2)
# True

print(100 in list2)
# False


# not in
# Returns True if an item is not present(not a member) of the iterable

print('Archana' not in list1)
# False

print('Krishna' not in list1)
# True


print(30 not in list2)
# False

print(100 not in list2)
# True