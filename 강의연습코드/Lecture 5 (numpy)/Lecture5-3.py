#arrays using numpy

#must install using "pip install numpy" in the terminal
import numpy as np #import numpy with the name np

arr1 = np.array([0, 2, 5, 7])
print(type(arr1))
#<class 'numpy.ndarray'>
print(arr1)
print()
#[0 2 5 7]
print(arr1.ndim) #차원수 dimensions in array
#1
print(arr1.shape) #각 차원의 크기 size per dimension
#(4,)
print(arr1.dtype) #요소 자료형 variable type
#int32
print(arr1.size) #전체 요소 개수 total number of elements
#4
print()

arr1 = np.array([[1, 2, 3,], [4, 5, 6]])
print(type(arr1))
#<class 'numpy.ndarray'>
print(arr1)
print()
#[[1 2 3] [4 5 6]]
print(arr1.ndim) #차원수 dimensions in array
#2
print(arr1.shape) #각 차원의 크기 size of array per dimension
#(2, 3)
print(arr1.dtype) #요소 자료형 variable type
#int32
print(arr1.size) #전체 요소 개수 total number of elements
#6