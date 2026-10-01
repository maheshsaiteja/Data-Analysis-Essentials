#C.Array of ones
#to create ones of an array there is a special function called np.ones(shape of the array)
import numpy as np
print("Array of Ones")
print("\n")
#prepare 1d one array
print("1d one array")
one_arr=np.ones(5)
print(one_arr)
#prepare 2d one array
print("2d one array")
one_2darr=np.ones([2,3])
print(one_2darr)
#prepare 3d one array
print("3d one array")
one_3darr=np.ones([1,4,3])
print(one_3darr)
#Attributes
print("\nAttributes for 1d array")
print("shape:",one_arr.shape)
print("Data type:",one_arr.dtype)
print("Dimension:",one_arr.ndim)
print("\nAttributes for 2d array")
print("shape:",one_2darr.shape)
print("Data type:",one_2darr.dtype)
print("Dimension:",one_2darr.ndim)
print("\nAttributes for 3d array")
print("shape:",one_3darr.shape)
print("Data type:",one_3darr.dtype)
print("Dimension:",one_3darr.ndim)

