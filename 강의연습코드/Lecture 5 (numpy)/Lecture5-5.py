import numpy as np

#create an array with the range(5) in ascending order
# 0, 1, 2, 3, 4
arr = np.arange(5)
print(type(arr))
#<class 'numpy.ndarray'>
print(arr)
#[0 1 2 3 4]
print(arr.ndim)
#1
print(arr.shape)
#(5,)
print(arr.dtype)
#int32
print(arr.size)
#5
print()

#create an starting from 3 - 10 with a skip of 2
# 3, 5, 7, 9
arr = np.arange(3, 10, 2)
print(type(arr))
#<class 'numpy.ndarray'>
print(arr)
#[3 5 7 9]
print(arr.ndim)
#1
print(arr.shape)
#(4,)
print(arr.dtype)
#int32
print(arr.size)
#4
