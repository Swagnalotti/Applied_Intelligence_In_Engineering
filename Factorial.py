def factorial(number):
    fac = 1
    for n in range(1, number + 1):
        fac = fac * n
    return fac

number = int(input("Enter your number: "))

print(f"{number}! = {factorial(number)}")