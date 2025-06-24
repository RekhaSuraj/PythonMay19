# Identity operators:
# These also are used usually for iterables 
# There are 2 types - is, is not

# is - checks to see if both objects are the same or not. Returns True if both are same object(pointing to the same memory location)

list1 = [10,12,14]
list2 = [10,12,14]

# id(<object>) - method which returns the address of the object
print(id(list1))
print(id(list2))

# 13 digit number - id
# 1769917436288
# 1769917438144

print(list1 is list2)
# False

# is not
# Returns True if both are not same object(not pointing to the same memory location or both having different ids)

print(list1 is not list2)
# True