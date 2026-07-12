import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr % 2 == 1)

print(x)