# slicing: 

# Positive slicing
# We use slicing to fetch a specific part of a string
# Syntax : [start:stop:step] index
# start : Refers from where to start slicing, If we dont specify, it will take start index by default
# stop : Refers till where to stop slicing, If we dont specify, it will take last index by default which is n-1
# step(Jump) : Refers to the jumps or steps we need to take, If we dont specify, it will take as 1

# It’s important to understand that the specified sub-portion is inclusive of the element at the 
# starting index and exclusive of the element at the ending index. 
# In other words, we can say that the element at the starting index is part of the result, 
# while the element at the ending index is not.

quote = "Happiness is everything"

# Fetch 'Happi' from the above string
print(quote[0:5])
# Happi

# Sepcified start and stop index
# Fetch 'is every'
print(quote[10:18])
# is every

# Start index not specified: It will take 0(start index) by default
print(quote[:5])
# Happi


# Fetch 'thing'
print(quote[18:23])
# thing

# If we dont specify stop index: It will take the full length of the string
print(quote[18:])
# thing

# without specifying any values
print(quote[::])
# Happiness is everything

# Specify step or jump to 2
print(quote[::2])
# Hpiesi vrtig

# Specify step or jump to 3 with start index
print(quote[2::3])
# pnssvyi
