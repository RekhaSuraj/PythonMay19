# hierarchical inheritance
print('hierarchical inheritance')

class A:
    i = 10


class B(A):
    j = 20


class C(A):
    k = 3


print(C.i)
print(C.k)
print()
print(B.i)
print(B.j)

# 10
# 3
#
# 10
# 20

# Hybrid inheritance
print('hybrid')
class A:
    i = 10

class B(A):
    j = 20

class C(A):
    k = 30


class D(B,C):
    pass


print(D.i)
print(D.j)
print(D.k)

# 10
# 20
# 30