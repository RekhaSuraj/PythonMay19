# Functions

# There are two types of functions :
# 1).Pre-defined functions
# Examples : print(),sum(),max(),min().........

# 2).User Defined Functions

# What is function ?
# Python Functions is a block of statements that perform/return the specific task.
# The idea is to put some commonly or repeatedly done tasks together and make a function
# so that instead of writing the same code again and again for different inputs,we can call the function

# To define user function by using def keyword

# def functionName():
#     statement...1
#     statement...2
#     statement...N
# FunctionName()

print('Function definition')
# Creating a function:
def hello_fun(): #function definition with colon
    print('hello world') #statements inside function


# Calling a function
print('function call below')
hello_fun()
print('After function call')

print(type(hello_fun))

# Function definition
# function call below
# hello world
# After function call
# <class 'function'>


