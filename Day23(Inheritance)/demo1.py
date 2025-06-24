# static methods:
# A @staticmethod is a method inside a class that:

# Does not need access to self (object).
# Does not need access to cls (class).

# It behaves like a normal function, but is put inside a class for organization.
# When to use @staticmethod:
# When the method doesn’t depend on class or object data.
# When you want to group utility functions logically inside a class.

class Aritmetic_tool:

    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def multiply(a,b):
        return a * b


v1 = Aritmetic_tool.add(10,20)
print(v1)
# 30


v2 = Aritmetic_tool.multiply(7,12)
print(v2)
# 84