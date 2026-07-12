import numpy as np

# First matrix (3x3)
A = np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

# Second matrix (3x4)
B = np.array([
  [7,14,31,4],
  [2,7,5,-9],
  [3,-1,5,13]
])

# Third matrix (4x2)
C = np.array([
  [1,2],
  [4,5],
  [7,8],
  [3,1]
])

# Matrix multiplication
result = A @ B @ C

print(result)

D = np.array([
    [1, 2],
    [3, 4]
    ])

print(f"{np.linalg.det(D) : .2f}")
print(np.linalg.inv(D))