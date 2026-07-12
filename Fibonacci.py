def fib(num):
    if num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

for i in range(1, 10):
    print(f"Fibonacci of {i} = {fib(i)}")