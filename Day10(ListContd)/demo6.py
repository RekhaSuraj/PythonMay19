import sys
l1 = [10,20,30,40,50]
t1 = (10,20,30,40,50)

# getsizeof() - Return the size of object in bytes
print('List size',sys.getsizeof(l1))
print('Tuple size',sys.getsizeof(t1))

# List size 104
# Tuple size 80

# Syntax Differences
# Feature	        List	                    Tuple
# Declaration	    my_list = [1, 2, 3]	        my_tuple = (1, 2, 3)
# Mutability	    Mutable (Changeable)	    Immutable (Unchangeable)
# Performance	    Slower (More Memory)	    Faster (Less Memory)
# Methods	        More(e.g., append(),
#                   remove())	                Fewer (Only count(), index())
# Use Cases	        When data changes often	    When data remains fixed