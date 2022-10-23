import numpy as np

print("index and slicing")
arr = np.arange(12).reshape(3, 4)
print(arr)
#[[0 1 2 3][4 5 6 7][8 9 10 11]]
print(arr[1])
#[4 5 6 7]
print(arr[1][1:3])
#[5 6]
print(arr[2][1])
#9
#this is the same as arr[2][1]
#print several values at once into an array
#[2][1] and [1][3]
print(arr[[2, 1],[1, 3]])
#[1 13]
print()

print("slicing into rows and columns")
print(arr)
print()

print(arr[0:2])#slice the rows
print()

print(arr[0:2, 1:3])    #slice row and columns
print()

print(arr[:, 1:3]) #only slice columns