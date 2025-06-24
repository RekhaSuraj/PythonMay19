# Default Arguments

# In a function, arguments can have default values.
# We assign default values to the argument using the ‘=’ (assignment) operator at the time of function definition(declaration).
# You can define a function with any number of default arguments.

def details(name='Test',age=25,salary=25000,location='BLR'):
    print(f'Name:{name}')
    print(f'Age:{age}')
    print(f'Salary:{salary}')
    print(f'Location:{location}')


# If we do not pass any arguments, default values will be assigned from the function definition
details()
# Name:Test
# Age:25
# Salary:25000
# Location:BLR

print()
# If we want to change or override the default values
details('Archana')

# Name:Archana
# Age:25
# Salary:25000
# Location:BLR

# Passing 3 arguments
print()
details('Archana',25,location='Bangalore')
# Name:Archana
# Age:25
# Salary:25000
# Location:Bangalore

print()
# Pass all arguments - override
details('Archana',28, 50000,location='Kerala')
# Name:Archana
# Age:28
# Salary:50000
# Location:Kerala