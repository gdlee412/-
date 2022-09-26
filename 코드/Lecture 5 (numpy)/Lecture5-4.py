import numpy as np
#create an array with 5 zeroes
arr = np.zeros(5)
print(type(arr))
#<class 'numpy.ndarray'>
print(arr)
#[0. 0. 0. 0. 0.]
print(arr.ndim)
#1
print(arr.shape)
#(5,)
print(arr.dtype)
#float64
print(arr.size)
#5
print()

#create 2d array of zeroes
arr = np.zeros((4, 2))
print(type(arr))
#<class 'numpy.ndarray'>
print(arr)
#[[0. 0.][0. 0.][0. 0.][0. 0.]]
print(arr.ndim)
#2
print(arr.shape)
#(4,2)
print(arr.dtype)
#float64
print(arr.size)
#8
print()

#array full of ones and change type to int
arr = np.ones(5, dtype=int)
print(type(arr))
#<class 'numpy.ndarray'>
print(arr)
#[1 1 1 1 1]
print(arr.ndim)
#1
print(arr.shape)
#(5,)
print(arr.dtype)
#int32
print(arr.size)
#5