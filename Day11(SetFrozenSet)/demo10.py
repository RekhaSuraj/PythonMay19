# Set Math Functions
# difference(iterable) - Return the difference of two or more sets as a new set.
# (i. e. all elements that are in this set but not the others.)
A = {1,2,3,4}
B = {1,2,3}

C = A.difference(B)
print(C)

A.difference_update(B)
print('A',A)
# A {4}
print('B',B)
# B {1, 2, 3}

# When both sets have same values, difference will return an empty set
X = {10,20,30}
Y = {10,20,30}
Z = X.difference(Y)
print(Z)
# set()


# intersection - Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
s1 = {1,2,3,4,5}
s2 = {1,2,3,6}
s3 = s1.intersection(s2)
print(s3)

#  union - Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
s4 = s1.union(s2)
print(s4)
# {1, 2, 3, 4, 5, 6}

# issubset() - Report whether another set contains this set.
s1 = {1,2,3,4,5}
s2 = {1,2,3}
print(s2.issubset(s1))
# True

s1 = {1,2,3,4,5}
s2 = {1,2,3,99}
print(s2.issubset(s1))
# False

# Returns True when both sets have same values
s1 = {1,2,3}
s2 = {1,2,3}
print(s1.issubset(s2))
# True

# superset() - Report whether this set contains another set
ss1 = {1,2,3,4,5}
ss2 = {1,2,3}
print('superset',ss1.issuperset(ss2))
# superset True
