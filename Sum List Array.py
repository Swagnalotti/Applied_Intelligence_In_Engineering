import numpy as np
import time

large_list = list(range(1000000000))
large_array = np.arange(1000000000, dtype=np.int64)

start = time.time()
sum_list = sum(large_list)
print(f"Python list sum: {sum_list}, Time: {time.time() - start:.6f} seconds")

start = time.time()
sum_array = np.sum(large_array)
print(f"NumPy array sum: {sum_array}, Time: {time.time() - start:.6f} seconds")