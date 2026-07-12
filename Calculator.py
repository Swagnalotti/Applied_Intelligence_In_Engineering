import math

def menu():
    print("Available operations")
    print("\t1- Addition")
    print("\t2- Subtraction")
    print("\t3- Multiplication")
    print("\t4- Division")
    print("\t5- Factorial")
    print("\t6- Summation")
    print("\t7- Is prime?")
    print("\t8- Quadratic Equation")

def factorial(number):
    fac = 1
    for n in range(1, number + 1):
        fac = fac * n
    return fac

def summation(number):
    sum = 0
    for n in range(1, number + 1):
        sum = sum + n
    return sum

def is_prime(number):
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True

def quadratic_equation(a, b, c):
    determinant = b ** 2 - 4 * a * c

    if determinant < 0:
        print("The quadratic equation has no real roots.")
    else:
        x1 = (-b + math.sqrt(determinant)) / (2 * a)
        x2 = (-b - math.sqrt(determinant)) / (2 * a)
        print(f"x1 = {x1: .2f}, x2 = {x2: .2f}")

another_operation = "y"

while another_operation == "y" or another_operation == "Y":
    menu()
    operation = int(input("Select an operation: "))
    if 5 > operation > 0:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if operation == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        else:
            print(f"{num1} / {num2} = {num1 / num2: .6f}")

    elif 6 >= operation >= 5:
        number = int(input("Enter a number: "))
        if operation == 5:
            print(f"{number}! = {factorial(number)}")
        else:
            print(f"sum({number}) = {summation(number)}")

    elif operation == 7:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"{number} is prime!")
        else:
            print(f"{number} is not prime!")

    elif operation == 8:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        quadratic_equation(a, b, c)

    else:
        print("Invalid operation!")

    another_operation = input("Enter Y/y to perform another operation: ")