#c.Broadcasting in NumPy Arrays
# Broadcasting means performing operations on arrays of different shapes.
# NumPy automatically expands the smaller array to match the shape of the larger array.

import numpy as np

# creating 2d array
twoD_arr = np.array([[1,2,3],[4,5,6]])
oneD_arr = np.array([10,20,30])

print("\nOriginal 1D Array:")
print(oneD_arr)

print("Original 2D Array:")
print(twoD_arr)

# Broadcasting addition
addition_res = twoD_arr + oneD_arr
print("\nBroadcasting Addition:\n", addition_res)

# Broadcasting subtraction
subtraction_res = twoD_arr - oneD_arr
print("\nBroadcasting Subtraction:\n", subtraction_res)

# Broadcasting multiplication
multiplication_res = twoD_arr * oneD_arr
print("\nBroadcasting Multiplication:\n", multiplication_res)

# Broadcasting division
division_res = twoD_arr / oneD_arr
print("\nBroadcasting Division:\n", division_res)
