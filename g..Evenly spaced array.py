#G.Evenly spaced array
import numpy as np
#using .arrange from 10,30 will be print with gapping value 3
arrng_arr=np.arange(10,30,5)
print("Evenly spaced array\n")
print(arrng_arr)
#using .linspace from 10,30 in this range i want print 5 values
lin_arr=np.linspace(10,30,5)
print(lin_arr)
#Attributes
print("Lin_arr")
print("shape:",lin_arr.shape)
print("DataType:",lin_arr.dtype)
print("Dimensions:",lin_arr.ndim)
print("Size:",lin_arr.size)
print("\narrng_arr")
print("shape:",arrng_arr.shape)
print("DataType:",arrng_arr.dtype)
print("Dimensions:",arrng_arr.ndim)
print("Size:",arrng_arr.size)
