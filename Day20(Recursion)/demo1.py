# Recursion - A function calling itself
import sys
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.

# What is the capacity of interpreter?
# To fetch/read
print(sys.getrecursionlimit())
# 1000

# To set
# sys.setrecursionlimit(100)
def Call():
    print('Hello')
    Call()

# Call()
# RecursionError: maximum recursion depth exceeded