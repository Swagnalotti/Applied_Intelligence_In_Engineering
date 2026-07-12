import time

# O(n*n)
def function(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum = sum + i

# O(n)
def add_up(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + 1
    return sum

# O(1)
def add_up_formula(n):
    sum = n * (n + 1) / 2
    return sum

num = int(input("Enter n: "))
start_time = time.time()
add_up(num)
print(f"Time to sum numbers from 0 - {num}: {time.time() - start_time: .4f} sec.")

start_time = time.time()
add_up_formula(num)
print(f"Time to sum numbers from 0 - {num}: {time.time() - start_time: .4f} sec.")