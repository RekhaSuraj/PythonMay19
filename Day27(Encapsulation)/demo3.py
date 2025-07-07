# Private access specifier
# Private :
# Private members are similar to protected members,
# the difference is that the class members declared private should neither be accessed outside
# the class nor by any base class.
# In Python, there is no existence of Private instance variables that cannot be accessed
# except inside a class.
#
# However, to define a private member prefix the member name with double underscore “__”.

class Student:

    def __init__(self, Name, Age):
        self.__name = Name
        self.__age = Age

    def __display(self):
        print(f'Name:{self.__name}')
        print(f'Age:{self.__age}')

    def show(self):
        self.__display()


obj_Student = Student("Radha",25)
obj_Student.show()
