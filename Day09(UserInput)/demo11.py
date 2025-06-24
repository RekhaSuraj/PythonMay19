# sort() and sorted()
list1 = [40,20,12,8,35,50,29]
# list1.sort()
# print(list1)
# By default sort() - arranges items in ascending order
# [8, 12, 20, 29, 35, 40, 50]

# If we want to sort in descending order, reverse=True
# list1.sort(reverse=True)
# print(list1)
# [50, 40, 35, 29, 20, 12, 8]

# sorted() - Return a new list containing all items from the iterable in ascending order.
# new_list = sorted(list1)
# print('new List after sorted',new_list)
# print('original list',list1)

# new List after sorted [8, 12, 20, 29, 35, 40, 50]
# original list [40, 20, 12, 8, 35, 50, 29]

# If we want to sort in descending order using sorted()
desc_list = sorted(list1,reverse=True)
print(desc_list)
# [50, 40, 35, 29, 20, 12, 8]

# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)

# hw -
# list1.count()
# list1.copy()

# print(help(list.count))
print(help(list))

# Help on method_descriptor:
#
# count(self, value, /)
#     Return number of occurrences of value.
