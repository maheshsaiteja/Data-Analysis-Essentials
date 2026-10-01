#e.Flattening a Numpy Array (flatten())
# Flattening a numpy array is nothing but converting any nD array into a 1D array using flatten().

import numpy as np
# Creating 2D array

twoD_arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

print("Original 2D Array is:")
print(twoD_arr)

print("Dimensions of Original Array are:",twoD_arr.ndim)

print("Shape of Original Array is:",twoD_arr.shape)

print("Size of Original Array is:",twoD_arr.size)

# Convert 2D array into 1D array using flatten()

flatten_arr = twoD_arr.flatten()

print("\nFlatten Array is:")
print(flatten_arr)

print("Dimensions of Flatten Array are:",flatten_arr.ndim)

print("Shape of Flatten Array is:",flatten_arr.shape)

print("Size of Flatten Array is:",flatten_arr.size)
