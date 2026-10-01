# f. Transpose of a Numpy Array (.T or transpose())

# Transpose of a numpy array means converting rows into columns and columns into rows by using .t or transpose() function
 
import numpy as np

# Creating a 2D array

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Original Array is:")
print(arr)
#Attributes of original array
print("Dimensions of Original Array are:",arr.ndim)

print("Shape of Original Array is:",arr.shape)

print("Size of Original Array is:",arr.size)

# Transpose of array using .T

transpose_arr = arr.T

print("\nTranspose Array using .T is:")
print(transpose_arr)

# Transpose of array using transpose()

transpose_arr2 = np.transpose(arr)

print("\nTranspose Array using transpose() is:")
print(transpose_arr2)

#Attributes of tranpose array
print("Dimensions of Transpose Array are:",transpose_arr.ndim)

print("Shape of Transpose Array is:",transpose_arr.shape)

print("Size of Transpose Array is:",transpose_arr.size)


