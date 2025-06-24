# print(help('lambda'))
# lambda_expr  "lambda" [parameter_list] ":" expression
# Lambda expressions (sometimes called lambda forms) are used to create
# anonymous(nameless) functions. The expression "lambda parameters: expression"
# yields a function object.  The unnamed object behaves like a function

# object defined with:
# def <lambda>(parameters):
#        return expression

v = lambda a: a+1
print(v(5))
# 6

print(type(v))
# <class 'function'>


m = lambda a,b:a*b
print(m(10,4))
# 40

# In a single line
# print('prod',(lambda a,b:a*b(5,6)))
# # <function <lambda> at 0x000001B057C65300>

print((lambda a,b:a*b)(5,4))
# 20

# Taking input from user
print((lambda x,y:x+y)(int(input("enter first number")),int(input('Enter second number'))))
# enter first number10
# Enter second number25
# 35


