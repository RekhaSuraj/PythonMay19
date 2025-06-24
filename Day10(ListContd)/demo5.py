# Tuple methods - Allows only 2 methods
t1 = (20,30,40,50,60,'hi','welcome',30,40)

# count() - number of occurrences of the item in the tuple
print(t1.count(30))
# 2

#index () - Return first index of value.
print(t1.index(30))
# 1

print(t1.index(30,2))
# 7

# If we try to access an item which is not in the tuple
print(t1.index(100))
# ValueError: tuple.index(x): x not in tuple




