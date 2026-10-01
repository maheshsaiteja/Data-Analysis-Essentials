#F.Imatrix in Numpy
#imatrix in numpy is created by using np.eye(size of n*n matrix)
import numpy as np
#creating 1D matrix
oneD_imat=np.eye(3)
print("Imatrix in Numpy\n")
print("1D marix")
print(oneD_imat)
#creating 2D matrix
twoD_imat=np.eye(5,5)
print("\n2D marix")
print(twoD_imat)
#creating 3D matrix
threeD_imat = np.array([np.eye(4), np.eye(4), np.eye(4)])
print("\n3D matrix")
print(threeD_imat)
#Attributes
print("\n1D marix")
print("Shape:",oneD_imat.shape)
print("DataType:",oneD_imat.dtype)
print("Dimensions:",oneD_imat.ndim)
print("Size:",oneD_imat.size)

print("\n2D marix")
print("Shape:",twoD_imat.shape)
print("DataType:",twoD_imat.dtype)
print("Dimensions:",twoD_imat.ndim)
print("Size:",twoD_imat.size)

print("\n3D marix")
print("Shape:",threeD_imat.shape)
print("DataType:",threeD_imat.dtype)
print("Dimensions:",threeD_imat.ndim)
print("Size:",threeD_imat.size)

