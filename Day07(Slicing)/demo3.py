# -ve slicing:
# IMP: Start index should always be smaller than the stop index. 
# If the start index is greater than stop index, we will get an empty string
quote = 'Python is a high level programming language'

# without specifying stop index
# Fetch language using -ve slicing
print(quote[-8:])

# Fetch program using -ve slicing
print(quote[-20:-13])
# program

# without specifying stop index
print(quote[-25::])
# evel programming language

# empty string if we give start index greater than stop index:
print(quote[5:1])