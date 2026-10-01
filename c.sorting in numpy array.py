# c. Sorting in NumPy Array
# Sorting a NumPy array means arranging elements in ascending order using the np.sort() function.

import numpy as np


# 1D Array Sorting

oneD_arr = np.array([2, 3, 9, 5])

print("\nOriginal 1D Array:")
print(oneD_arr)

sort_arr = np.sort(oneD_arr)

print("Sorted 1D Array:")
print(sort_arr)


# 2D Array Sorting

twoD_arr = np.array([[1, 8, 4],
                     [9, 5, 23],
                     [7, 6, 3]])

print("\nOriginal 2D Array:")
print(twoD_arr)

# Sort 2D Array Column-wise

sort2D_column = np.sort(twoD_arr, axis=0)

print("\nSorted 2D Array - Column-wise:")
print(sort2D_column)

# Sort 2D Array Row-wise

sort2D_row = np.sort(twoD_arr, axis=1)

print("\nSorted 2D Array - Row-wise:")
print(sort2D_row)





# Sort All Elements of 2D Array

sort_all = np.sort(twoD_arr, axis=None)

print("\nAll Elements Sorted:")
print(sort_all)