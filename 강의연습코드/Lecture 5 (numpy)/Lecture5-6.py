import numpy as np

print("arrange")
arr = np.arange(12)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr.ndim)
#[1]
print(arr.shape)
#(12,)
print()

#reshape arr into a 2D array with 3, 4 as rows and columns
#we have to give the right rows and columns to match the number of elements
print("reshaping")
arr2 = arr.reshape(3, 4)
print(arr2)
#[[ 0  1  2  3][ 4  5  6  7][ 8  9 10 11]]
print(arr2.ndim)
#2
print(arr2.shape)
#(3,4)
print()

#remove the last dimension
print("removing a dimension")
arr2 = arr.reshape(-1)
print(arr2)
#[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr2.ndim)
#[1]
print(arr2.shape)
#(12,)
print()

#arrange and reshape at the same time
print("reshaping")
arr = np.arange(12).reshape(3,4)
print(arr)
print()
#[[0 1 2 3][4 5 6 7][8 9 10 11]]

#reshape and adjust the rows such that the columns are 2
#add -1 if you want program to adjust either the row or columns
#the other one should be assigned
print("reshape with auto adjusting")
arr = arr.reshape(-1, 2)
print(arr)
#[[0 1][2 3][4 5][6 7][8 9][10 11]]
print(arr.ndim)
#2
print(arr.shape)
#(6, 2)
print()