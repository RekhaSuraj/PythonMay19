# Multiple inheritance

print('Multiple')
class A:
    i = 10


class B:
    j = 20


class C(A,B):
    pass


print(C.i)
print(C.j)

# Multiple
# 10
# 20

print()
# With same variable names

class A:
    i = 10


class B:
    i = 20


class C(A,B):
    pass

print(C.i)
# 10

#
print()
class A:
    i = 10

class B:
    i = 20


class C(B,A):
    pass

print(C.i)
# 20

# If both parents have same variable name, only the first parent's value will be considered.