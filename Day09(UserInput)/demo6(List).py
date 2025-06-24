# List - Sequence datatype (inbuilt)

# collection of elements
# it can be homogeneous(same datatype) or heterogeneous(different datatypes)
# each element is stored under a cell
# each cell has number--> index
# if list contains n number of elements then index will be 0 to n-1
# any index more than n-1 --> we get error out of range...

# to access element from list we use index --> listname[index]


#Why we are using list ?
# We can store Multiple different datatypes with in a single variable using the list.
# List have some unique methods, Append, remove
# using  above methods we can modify , Access the list value

# List is a Mutable datatype (Changeable) After creation
# List is an ordered collection of datatype (having a Unique index values) seperated by comma's
# List is enclosed in Square brackets.

# string is immutable, whereas list is mutable

# ex1:syntax: listname = [list_elements]

list1 = [10,20,30,40,50] #homogeneous (same datatype)
print(type(list1))
# <class 'list'>

list2 = [20.5,3+5j,'hi','45',60] # heterogeneous(different datatypes)
print(type(list2))
# <class 'list'>

print(list2)
# [20.5, (3+5j), 'hi', '45', 60]





