import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

#1D Array
a = np.array([1, 2, 3, 4, 5])

#2D Arrays
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#3D Arrays
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.7], dtype=np.float64)
c = np.array([True, False], dtype=bool)

print(a.dtype)
print(b.dtype)
print(c.dtype)

#Assign a floating-point data type
a = np.array([1.5, 2.7])

#Cast as integer (floor)
b = a.astype(int)

print(a)
print(b)

#1D Array
a = np.array([1, 2, 3, 4, 5])

#2D Arrays
b = np.array([[1, 2, 3], [4, 5, 6]])

#3D Arrays
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#First element in the row
print(a[0])

#Element at second row, third column
print(b[1, 2])

#Element at second matrix, second row, third column
print(c[1, 1, 2])