# WEEk-4:Indexing and slicing of Numpy Array
#A.Slicing 1-D NumPy arrays
#Slicing 1-D NumPy arrays allows you to extract specific portions of data by defining a range of indices using the [start:stop:step] basic syntax.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Print the array
print("Original array:")
print(arr)

# 1. Basic range slicing
print("\nBasic range slicing:")
print(arr[1:5])

# 2. Omitting start or stop
print("\nFrom index 3 to the end:")
print(arr[3:])

print("\nFrom the start to index 4:")
print(arr[:4])

print("\nCopy the whole array:")
print(arr[:])

# 3. Using step size (striding)
print("\n0 to 6 for every step 2:")
print(arr[0:6:2])

# Negative slicing
print("\nSlice from 3rd from last to the last element:")
print(arr[-3:])

# Reverse the array
print("\nReverse the array:")
print(arr[::-1])