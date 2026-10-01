
#c.Slicing 3-D NumPy arrays 
# slicing a 3-D NumPy array is similar to slicing a 2-D array, but with an additional dimension.
import numpy as np

# Creating a 3D array
arr = np.arange(24).reshape(2, 3, 4)

print("Original 3D array:")
print(arr)

# Slicing 3D array

print("\nSelect the first matrix (index 0):")
print(arr[0, :, :])

print("\nSelect the second row:")
print(arr[:, 1, :])

print("\nThird column:")
print(arr[:, :, 2])

print("\nTop-right sub-cube in first matrix:")
print(arr[0, 0:2, 2:4])

