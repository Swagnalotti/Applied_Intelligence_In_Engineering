def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

#n! = n x (n - 1)!
#0! = 1

def recursive_factorial(num):
    if num <= 1:
        return 1
    return num * recursive_factorial(num - 1)