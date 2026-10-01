# d. Reshaping a Numpy Array
#d.reshape a numpy array 
# to reshape any array into another array there is a function know as reshape()

import numpy as np

# Creating a 1D array with 9 elements

oneD_arr = np.array([1,2,3,4,5,6,7,8,9])

print("oneD array is:")
print(oneD_arr)

print("Shape of OneD array before reshape :",oneD_arr.shape)

# now using reshape() convert 3*3

reshape_arr = np.reshape(oneD_arr, (3,3))

print("Reshaped array is:")
print(reshape_arr)
print("Shape of OneD array after reshape:",reshape_arr.shape)

# Creating a 2D array

twoD_arr = np.array([[1,2,3,4],[5,6,7,8]])

print("TwoD array is:")
print(twoD_arr)

print("Shape of TwoD array before reshape:",twoD_arr.shape)

reshape1 = np.reshape(twoD_arr, (4,2))

print("Reshaped TwoD array is:")
print(reshape1)

print("Shape of TwoD array after reshape:",reshape1.shape)
