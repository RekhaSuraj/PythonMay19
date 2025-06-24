# Mixing Positional and Keyword arguments

# Rule is first positional arguments should be declared first

def details(eName,eAge,eSalary,eLocation):
    print(f'Name:{eName}')
    print(f'Age:{eAge}')
    print(f'Salary:{eSalary}')
    print(f'Location:{eLocation}')


# details(eAge=25,eName='GRK',50000,'Kerala')
# SyntaxError: positional argument follows keyword argument

details('Archana',25,eLocation='Kerala',eSalary=50000)
# Name:Archana
# Age:25
# Salary:50000
# Location:Kerala