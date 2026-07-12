import random

fruit_list = ["apple", "banana", "cherry"] # List of strings
print(fruit_list)

a = [1, -3, 9, 4, 102] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)

a = [-1, 6, 99, 100, 50, -99, 1000, 6]
b = ["Sarah", "John", "Peter"]

print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(sorted(a))

#generate a list of size n of random integers in range 0 - x
list = [random.randint(1, 100) for i in range(1000)]

print(list)
print(sorted(list))
print(max(list))
print(min(list))
print(sum(list))
print(len(list))

a = [-1, 6, 99, 100, 50, -99, 1000, 6]

print(a[1 : 4])
print(a[0 : len(a)])