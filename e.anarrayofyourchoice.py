#E.An array of your choice
import numpy as np
#Creating 1D choice array
oneD_charr=np.full((6),3)
print("An array of your choice\n")
print("1D array")
print(oneD_charr)
#Creating 2D choice array
twoD_charr=np.full((4,5),22)
print("2D array")
print(twoD_charr)
#Creating 3D choice array
threeD_charr=np.full((1,7,8),78)
print("3D array")
print(threeD_charr)

#Attributes
print("\n1D array")
print("Shape:",oneD_charr.shape)
print("DataType:",oneD_charr.dtype)
print("Dimensions:",oneD_charr.ndim)
print("Size:",oneD_charr.size)
print("\n2D array")
print("Shape:",twoD_charr.shape)
print("DataType:",twoD_charr.dtype)
print("Dimensions:",twoD_charr.ndim)
print("Size:",twoD_charr.size)
print("\n3D array")
print("Shape:",threeD_charr.shape)
print("DataType:",threeD_charr.dtype)
print("Dimensions:",threeD_charr.ndim)
print("Size:",threeD_charr.size)

