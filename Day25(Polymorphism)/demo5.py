class Test_overload:

    def add1(self,x,y=0,z=0):
        return x+y+z



obj_add1 = Test_overload()
print(obj_add1.add1(2))
# 2


print(obj_add1.add1(4,5))
# 9


print(obj_add1.add1(1,2,3))
# 6