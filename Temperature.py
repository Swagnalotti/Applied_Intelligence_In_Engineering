# C = (F - 32) * 5 / 9

def celcius(temp_f):
    return (temp_f - 32) * 5 / 9

print(f"24F is {celcius(24): .2f}C")
print(f"73F is {celcius(73): .2f}C")
print(f"91F is {celcius(91): .2f}C")
print(f"110F is {celcius(101): .2f}C")