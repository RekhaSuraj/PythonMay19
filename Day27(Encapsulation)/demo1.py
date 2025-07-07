# Encapsulation:

# Encapsulation : Wrapping data and methods within single unit.
# In Python, encapsulation refers to the bundling of data (attributes) and methods (functions)
# that operate on the data into a single unit, typically a class.
# It also restricts direct access to some components,
# which helps protect the integrity of the data and ensures proper usage.
# Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through
# an object’s methods

# There are 3 Access Specifiers(Modifiers) :
# 1.Public Access Specifier
# 2.Protected Access Specifier
# 3.Private Access Specifier


# 1.Public Access Specifier : Access from anywhere, Inside class, child class, Outside of class

class Employee:
    def __init__(self,Name,Age,Salary):
        self.name = Name #public variable1
        self.age = Age #public variable2
        self.salary = Salary #public variable3

    #public method (instance method)
    def display(self):
        print(f'Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}')


obj_Emp = Employee("Seetha",30,50000)
obj_Emp.display()

obj_Emp.name = 'Rama'
obj_Emp.display()

# Name:Seetha
# Age:30
# Salary:50000
# Name:Rama
# Age:30
# Salary:50000