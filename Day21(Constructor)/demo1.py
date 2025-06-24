# Constructors in Python

# In Python, a constructor is a special type of method used to initialize the object of a Class.
# The constructor will be executed automatically when the object is created. If we create three objects,
# the constructor is called three times and initialize each object.

# The main purpose of the constructor is to declare and initialize instance variables. It can take at least one argument that is self.
#  The __init()__ method is called the constructor in Python. In other words, the name of the constructor should be __init__(self).

# A constructor is optional, and if we do not provide any constructor, then Python provides the default constructor.
# Every class in Python has a constructor, but it's not required to define it.


# def __init__(self):
#     # body of the constructor

# def: The keyword is used to define function.
# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
# self: The first argument self refers to the current object.
# It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.

class Person:

    def __init__(self, p_name, p_age, p_gender):
        self.name = p_name #instance var1
        self.age = p_age   #instance var2
        self.gender = p_gender  #instance var3

        print(self.name,self.age, self.gender)


# created an object of class Person outside the class
ob_person = Person("Archana",25,'Female')
# Archana 25 Female

print()
# create one more object of class Person
ob_person1 = Person('Rama',35, 'Male')
# Rama 35 Male