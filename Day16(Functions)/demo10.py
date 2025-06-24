# Factorial of a number using functions

def fact_fun(num1):
    fact = 1
    for i in range(1,num1+1):
        fact = fact * i

    return fact


fact_res = fact_fun(5)
print(fact_res)
# 120


# hw - largest of 3 numbers using functions
# smallest number in a list [20,5,30,10,2,45] using functions
# length of a list using functions without using inbuilt len()





def largest_num(n1,n2,n3):
    if n1> n2 and n1> n3:
        print('n1 greater')
    elif n2>n1 and n2>n3:
        print('n2 greater')

    else:
        print('n3 greater')



n1 = 5
n2 = 10
n3 = 15
largest_num(n1,n2,n3)








