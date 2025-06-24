from multipledispatch import dispatch
# Overloading methods

class Arithmetic:

    @dispatch(int,int)
    def add(self,x,y):
        return x+y

    @dispatch(int,int,int)
    def add(self,x,y,z):
        return x+y+z

    @dispatch(int,int,int,int)
    def add(self,x,y,z,l):
        return x+y+z+l


obj_arith = Arithmetic()
print(obj_arith.add(1,2,3,4))

# 10

print(obj_arith.add(5,6))
# TypeError: Arithmetic.add() missing 2 required positional arguments: 'z' and 'l'

print(obj_arith.add(7,1,2))
# TypeError: Arithmetic.add() missing 1 required positional argument: 'l'

