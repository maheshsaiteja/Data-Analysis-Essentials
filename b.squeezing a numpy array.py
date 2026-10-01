# WEEK-3 : 
#b.Squeezing a NumPy Array
#Squeezing a NumPy array means removing dimensions of size 1 from an array using np.squeeze().
import numpy as np

print("Squeezing a NumPy Array\n")

# Squeeze a 2D Array
twoD_arr = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

print("Original 2D Array:")
print(twoD_arr)

print("Shape:", twoD_arr.shape)
print("Dimension:", twoD_arr.ndim)

# Apply squeeze
squ_twoD = np.squeeze(twoD_arr)

print("\nSqueezed 2D Array:")
print(squ_twoD)

print("Shape:", squ_twoD.shape)
print("Dimension:", squ_twoD.ndim)

# Squeeze a 3D Array

threeD_arr = np.arange(9).reshape(1, 3, 3)

print("\nOriginal 3D Array:")
print(threeD_arr)

print("Shape:", threeD_arr.shape)
print("Dimension:", threeD_arr.ndim)

# Apply squeeze
squ_threeD = np.squeeze(threeD_arr)

print("\nSqueezed 3D Array:")
print(squ_threeD)

print("Shape:", squ_threeD.shape)
print("Dimension:", squ_threeD.ndim)




