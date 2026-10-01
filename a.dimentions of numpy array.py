# week-2 the shape and reshaping of numpy array
#a.Dimensions of numpy array
# to get dimensions of any array we are using attribute is ndim()

import numpy as np

# Creating 1D, 2D, 3D array

arr1 = np.array([1,2,3,4,5,6,7,8,9])

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

arr3 = np.array(range(8)).reshape(2,2,2)

# Print arrays

print("1D array is:")
print(arr1)

print("2D array is:")
print(arr2)

print("3D array is:")
print(arr3)

# Attributes of dimensions

print("1D array dimensions are:", arr1.ndim)

print("2D array dimensions are:", arr2.ndim)

print("3D array dimensions are:", arr3.ndim)
