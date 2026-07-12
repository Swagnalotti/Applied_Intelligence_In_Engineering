import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    x1 = complex(real_part, imaginary_part)
    x2 = complex(real_part, -imaginary_part)

else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

print(f"Your equation roots are ({x1}, {x2})")