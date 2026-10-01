#4.d. Negative slicing of NumPy arrays
#Negative slicing in NumPy arrays uses negative indices (-1, -2, etc.) to extract a subset of elements by counting backwards from the end of the array.
#you can apply negative slicing to rows, columns, or both simultaneously 

import numpy as np

# 4. Negative slicing of NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original array:")
print(arr)

print("\nSlicing from 5th last to 2nd from last element:")
print(arr[-5:-2])

print("\nFrom last three elements:")
print(arr[-3:])

print("\nReverse the array:")
print(arr[::-1])


# Slicing from multidimensional array
arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\n2D array:")
print(arr2)

print("\nLast row:")
print(arr2[-1, :])

print("\nLast two columns:")
print(arr2[:, -2:])

print("\nSub matrix:")
print(arr2[-3:-1, -4:-2])