"""
Return Value From a Function
In Python, to return value from the function, a return statement is used. It returns the value of the expression following the return keyword.

Syntax of return statement

def fun():
    statement-1
    statement-2
    statement-3
    .
    .
    return [expression]
The return value is nothing but an outcome of function.

The return statement ends the function execution.
For a function, it is not mandatory/compulsory to return a value.
If a return statement is used without any expression, then the None is returned.
The return statement should be inside of the function block.
"""

# Function without return keyword gives None as output
# def fun_Test():
#     print('hello world')
#
#
# print(fun_Test())
# # None
#
# res = fun_Test()
# print(res)
# None


def greetings():
    return 'hello from GRK'


var1 = greetings()
print(var1)
# hello from GRK