# week-2 the shape and reshaping of numpy array
#b.shape of numpy array 
# to get shape of any array we use attribute is shape()
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

# Attributes of shape

print("1D array shape is:", arr1.shape)

print("2D array shape is:", arr2.shape)

print("3D array shape is:", arr3.shape)
