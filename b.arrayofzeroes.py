#B.Array of zeros
#to create zeros of an array there is a special function called np.zeros(shape of the array)
import numpy as np
#prepare to zero array
print("1d zero array")
zero_arr=np.zeros(5)
print(zero_arr)
#prepare 2d zero array
print("2d zero array")
zero_2darr=np.zeros([2,3])
print(zero_2darr)
#prepare 3d zero array
print("3d zero array")
zero_3darr=np.zeros([1,3,4])
print(zero_3darr)
#Attributes
print("Attributes for 1d array")
print("shape:",zero_arr.shape)
print("Data type:",zero_arr.dtype)
print("Dimension:",zero_arr.ndim)
print("Attributes for 2d array")
print("shape:",zero_2darr.shape)
print("Data type:",zero_2darr.dtype)
print("Dimension:",zero_2darr.ndim)
print("Attributes for 3d array")
print("shape:",zero_3darr.shape)
print("Data type:",zero_3darr.dtype)
print("Dimension:",zero_3darr.ndim)
