# Arguments
# Types of arguments
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable Length Arguments


# Positional Arguments:
# Positional arguments are those arguments where values get assigned to the arguments by their position when the function is called.
# For example, the 1st positional argument must be 1st when the function is called.
# The 2nd positional argument needs to be 2nd when the function is called, etc

def profile(Name, age):
    print(f'Name:{Name}')
    print(f'Age:{age}')

# Name and Age arguments must be assigned correctly
profile('Archana',25)

# If assigned wrong, it will lead to data mismatch/error
profile(25,'Archana')
