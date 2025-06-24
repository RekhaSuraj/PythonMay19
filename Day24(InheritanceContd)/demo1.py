# single inheritance
print('Single')
# parent class
class A:
    i = 10


# child class
class B(A):
    pass


print(B.i)
# 10

print("Multilevel")
# multilevel inheritance
class A:
    i = 10


class B(A):
    j = 20


class C(B):
    pass


print(C.i)
print(C.j)