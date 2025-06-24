# Calling instance variables using instance methods

# Instance method: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.
# Calling Instance Variables by using Instance method

class Mobile:

    def __init__(self, Name, Color, RAM, Make):
        print('Here')
        self.name = Name
        self.color = Color
        self.RAM = RAM
        self.make = Make

    # Instance method1
    def display(self):
        print(f'Name:{self.name}')
        print(f'Color:{self.color}')
        print(f'RAM:{self.RAM}')
        print(f'Make:{self.make}')

    # Instance method2
    def name_upper(self):
        return self.name.upper()

    # Instance method3
    def delete_make(self):
        del self.make


obj_Mobile = Mobile('Samsung','White',6,2025)
obj_Mobile.display()
# Here
# Name:Samsung
# Color:White
# RAM:6
# Make:2025

print()
print(obj_Mobile.name_upper())
# SAMSUNG

print()
obj_Mobile.delete_make()
obj_Mobile.display()

# Name:Samsung
# Color:White
# RAM:6
# AttributeError: 'Mobile' object has no attribute 'make'

