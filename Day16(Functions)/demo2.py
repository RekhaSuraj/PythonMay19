# Fibonacci series

first = 0
second = 1

print(first,second, end=' ')
for i in range(2,20):
    next = first + second
    print(next, end=' ')
    first = second
    second = next

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181