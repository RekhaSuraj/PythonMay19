# To pass parameters to functions
# Accepts 2 parameters
def add(num1,num2):
    print(num1 + num2)

# If we call the function without passing any parameters, we get the below error
# add()
# TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'


add(10,5)
# 15

add(20,30)
# 50