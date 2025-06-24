# Keyword arguments

# Arguments are passed by parameter names, so order does not matter.


def profile(eName,eAge):
    print(f'EmpName:{eName}')
    print(f'EmpAge:{eAge}')


profile(eName='Archana',eAge=25)
print()
profile(eAge=25,eName='Test')

# EmpName:Archana
# EmpAge:25
#
# EmpName:Test
# EmpAge:25