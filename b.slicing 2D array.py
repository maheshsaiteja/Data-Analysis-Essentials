#b.Slicing 2-D NumPy arrays
#To slice a 2-D NumPy array, separate the row and column slicing expressions
#with a comma inside a single set of square brackets:
#array[row_start:row_stop:row_step, col_start:col_stop:col_step]
import numpy as np

# Creating a 4x4 sample array
arr = np.arange(16).reshape(4, 4)

print("Original 2D array:")
print(arr)

# Slicing the array

print("\nGet the second row:")
print(arr[1, :])

print("\nThird column:")
print(arr[:, 2])

print("\nTop-left 2x2 block:")
print(arr[0:2, 0:2])

print("\nInner 2x2 block:")
print(arr[1:3, 1:3])

print("\nEvery second row, all columns:")
print(arr[::2, :])

print("\nEvery second column, all rows:")
print(arr[:, ::2])

print("\nLast two rows:")
print(arr[-2:, :])

print("\nReverse row order:")
print(arr[::-1, :])