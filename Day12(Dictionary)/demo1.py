# Dictionary - Is another inbuilt datatype in python

# using curly braces: dictionaries are created by enclosing the comma-separated
# Key:Value pairs inside the curly brackets
# Dictionaries are mutable(modified)

# create an empty dictionary
d1 = {}
print(type(d1))
# <class 'dict'>

# using constructor:
d2 = dict({1:'Kar',2:'Kerala',3:'AP',4:'MP'})
print(d2)
print(type(d2))
# {1: 'Kar', 2: 'Kerala', 3: 'AP', 4: 'MP'}
# <class 'dict'>

# Dictionary is heterogeneous, it can have different datatype
d3 = {'Name':['Archana','Shiva','Rama','Krishna'],
      'Age':(20,30,40,50),
      'Salary':{20000,30000,40000,50000}
      }
print(d3)
# {'Name': ['Archana', 'Shiva', 'Rama', 'Krishna'], 'Age': (20, 30, 40, 50), 'Salary': {20000, 30000, 50000, 40000}}