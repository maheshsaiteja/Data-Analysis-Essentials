#Week-5: Stacking and concatenating numpy array
#a.stacking ndarrays
#Stacking arrays means joining two or more arrays along a specified axis.
#we using functions are np.hstack() for Horizontal stacking np.vstack() for Vertical stacking

import numpy as np
#creating 2d array
twoD_arr1=np.array([[1,2],[3,4]])
twoD_arr2=np.array([[5,6],[7,8]])
print("Original 2D Arrays:")
print("Array1:")
print(twoD_arr1)
print("Array2:")
print(twoD_arr2)
#Horizantal 2D Array stacking
horizontal_2Dres=np.hstack((twoD_arr1,twoD_arr2))
print("\nHorizontal 2D Stack:\n", horizontal_2Dres)
#vertical 2D Array stacking
vertical_2Dres=np.vstack((twoD_arr1,twoD_arr2))
print("\nVertical 2D Stack:\n", vertical_2Dres)


# creating 3d array
threeD_arr1 =np.arange(9).reshape(1,3,3)
threeD_arr2 =np.arange(9).reshape(1,3,3)

print("\nOriginal 3D Arrays:")
print("Array1:")
print(threeD_arr1)
print("Array2:")
print(threeD_arr2)

# Horizontal 3D Array stacking
horizontal_3Dres = np.hstack((threeD_arr1,threeD_arr2))
print("\nHorizontal 3D Stack:\n", horizontal_3Dres)

# Vertical 3D Array stacking
vertical_3Dres = np.vstack((threeD_arr1,threeD_arr2))
print("\nVertical 3D Stack:\n", vertical_3Dres)
