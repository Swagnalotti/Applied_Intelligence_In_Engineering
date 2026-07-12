import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

sqrt_value = b * b - 4 * a * c

if sqrt_value < 0:
    print("Equation has no real roots")
else:
    x1 = (-b + math.sqrt(sqrt_value)) / (2 * a)
    x2 = (-b - math.sqrt(sqrt_value)) / (2 * a)

    print(f"Your equation roots are ({x1}, {x2})")