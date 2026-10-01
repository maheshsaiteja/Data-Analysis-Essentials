# WEEK-3 :Expanding and squeezing a Numpy Array 
#a.Expanding a NumPy Array
# Expanding a NumPy array means adding a new axis to an existing array using np.expand_dims(). It can be expanded row-wise or column-wise.

import numpy as np

#creating 1D array4


oneD_arr=np.array([5,6,7,8,9,10])

#print the array
print("Original 1D Array:")
print(oneD_arr)

#Dimensions
print("Dimensions of the 1d original array is:",oneD_arr.ndim)
print("Size of the 1d original array is:",oneD_arr.size)
print("Shape of the 1d original array is:",oneD_arr.shape)

#Expand the array using functions

#expand the 
# rows
expnd_rows=np.expand_dims(oneD_arr,axis=0)
#print the expanded array
print("\nExpanded Rows Of 1D Array:")
print(expnd_rows)
print("Dimensions of the expand rows array is:",expnd_rows.ndim)
print("Size of the expand rows array is:",expnd_rows.size)
print("Shape of the expand rows array is:",expnd_rows.shape)

#expand the columns
twoD_arr=np.array([[1,2,3,4],[5,6,7,8]])

#print array
print("\nOriginal 2D Array:")
print(twoD_arr)
#Attributes of 2d Array
print("Dimensions of 2D array is:",twoD_arr.ndim)
print("Size of 2D array is:",twoD_arr.size)
print("Shape of 2D array is:",twoD_arr.shape)

#attributes Of expanded column array

expnd_colmns=np.expand_dims(twoD_arr,axis=1)

print("\nExpanded Columns Of 2D Array:")
print(expnd_colmns)
print("Dimensions of the expand column array is:",expnd_colmns.ndim)
print("Size of the expand column array is:",expnd_colmns.size)
print("Shape of the expand column array is:",expnd_colmns.shape)