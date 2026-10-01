# b. Concatenating ndarrays
# Concatenating arrays means joining two or more arrays along a specified axis.
# We use np.concatenate() function for concatenating arrays.

import numpy as np

# creating 2d array
twoD_arr1 = np.array([[1,2],[3,4]])
twoD_arr2 = np.array([[5,6],[7,8]])

print("Original 2D Arrays:")
print("Array1:")
print(twoD_arr1)
print("Array2:")
print(twoD_arr2)

# Horizontal 2D Array concatenating
horizontal_2Dres = np.concatenate((twoD_arr1,twoD_arr2), axis=1)
print("\nHorizontal 2D Concatenation:\n", horizontal_2Dres)

# Vertical 2D Array concatenating
vertical_2Dres = np.concatenate((twoD_arr1,twoD_arr2), axis=0)
print("\nVertical 2D Concatenation:\n", vertical_2Dres)


# creating 3d array using arange
threeD_arr1 = np.arange(9).reshape(1,3,3)
threeD_arr2 = np.arange(9,18).reshape(1,3,3)

print("\nOriginal 3D Arrays:")
print("Array1:")
print(threeD_arr1)
print("Array2:")
print(threeD_arr2)

# Horizontal 3D Array concatenating
horizontal_3Dres = np.concatenate((threeD_arr1,threeD_arr2), axis=2)
print("\nHorizontal 3D Concatenation:\n", horizontal_3Dres)

# Vertical 3D Array concatenating
vertical_3Dres = np.concatenate((threeD_arr1,threeD_arr2), axis=1)
print("\nVertical 3D Concatenation:\n", vertical_3Dres)
