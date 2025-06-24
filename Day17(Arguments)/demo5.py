# Variable Length Arguments

# In Python, functions can accept a variable number of arguments using:
#
# *args → Variable-length positional arguments (Tuple)
# **kwargs → Variable-length keyword arguments (Dictionary)
#
# 1. Using *args (Multiple Positional Arguments)
# ✅ Allows a function to accept any number of positional arguments.
# ✅ Collects them into a tuple.

def profile(*args):
    print(args)
    for i in args:
        print(i)


profile('hello',10,'hi',20,'welcome',30,40)

# ('hello', 10, 'hi', 20, 'welcome', 30, 40)
# hello
# 10
# hi
# 20
# welcome
# 30
# 40



