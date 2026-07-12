import random

i = random.randint(0, 1000)
count = 1

while i != 555:
    i = random.randint(0, 1000)
    count = count + 1

print(f"Number of attempts: {count}")