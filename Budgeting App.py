income = int(input("Enter income: "))
tax = float(input("Enter tax: "))
rent = int(input("Enter rent: "))
health_insurance = int(input("Enter your health insurance: "))
employee_name = input("Enter your employee name: ")

net_income = (income - income * tax) - rent - health_insurance

print(40 * "-")
print(f"Dear {employee_name}")
print(f"Total income is ${income}")
print(f"Income after ({tax}) tax: ${income - income * tax}")
print(f"Rent: ${rent}")
print(f"Health insurance: ${health_insurance}")
print(f"Net income: ${net_income}")

if net_income <= 3000:
    print("Be careful 😔")
elif net_income <= 5000:
    print("You are good! 😀")
else:
    print("Time to invest! 😎🤑")

print(30 * " " + "Thank you!")
print(40 * "-")