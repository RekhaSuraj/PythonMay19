# Exception Handling:

# What are Exceptions?
# An exception is an event that occurs during the execution of programs that disrupt the normal flow of execution
# Risky code - A code which has the probability(chances) of getting error.
# During the execution, if there are any errors, it will throw error and stop the execution. To continue the execution, we should
# handle the exception.
#  (e.g., KeyError Raised when a key is not found in a dictionary.) An exception is a Python object that represents an error..
"""
The errors can be broadly classified into two types:

1.Syntax errors
2.Logical errors

Syntax error
The syntax error occurs when we are not following the proper structure or syntax of the language.
 A syntax error is also known as a parsing error.

When Python parses the program and finds an incorrect statement it is known as a syntax error.
 When the parser found a syntax error it exits with an error message without running anything.

Common Python Syntax errors:

Incorrect indentation
Missing colon, comma, or brackets

Putting keywords in the wrong place.

Logical errors, also known as semantic errors, occur when the code is syntactically correct but does not
produce the intended result. These errors are not detected by the interpreter and the program will run, but the output
will be incorrect. Common examples include: Using the wrong operator, Incorrectly implemented algorithm,
and Off-by-one errors in loops.
"""

# Types of terminations:
# 1. Normal termination (No error till end)
# 2. Abnormal termination (Error not handled)
# 3. Graceful termination (Error occurred but handled)


# syntax:
# try:
#     # risky code
# except:
#     # recovery code
#
# else:
#     # continue code
#
# finally:
#     # cleanup code
