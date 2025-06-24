# Class Variables:

# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

class Student:
    # Class variable
    school = 'ABC School'

    def __init__(self, s_name, s_age, s_class, s_gender):
        self.Name = s_name
        self.Age = s_age
        self.Class = s_class
        self.Gender = s_gender

    def display(self):
        print(f'Student Name: {self.Name}')
        print(f'Student Age: {self.Age}')
        print(f'Student Class: {self.Class}')
        print(f'Student Gender:{self.Gender}')


ob1 = Student('Rama',12,5,'M')
ob2 = Student('Seetha',16,10,'F')
ob3 = Student('Krishna',20, 12, 'M')
ob4 = Student('ABC',10,4,'F')

all_objs = [ob1,ob2,ob3,ob4]

for var1 in all_objs:
    print(f'Name:{var1.Name}')
    print(f'Age:{var1.Age}')
    print(f'Class:{var1.Class}')
    print(f'Gender:{var1.Gender}')
    print(f'School Name:{var1.school}')
    print()







