#Broadcasting in numpy
import numpy as np

#when arrays are multiplied, the program broadcasts (repeats the row/columns) such that both have the same rows and columns

arr = np.arange(4)
#[0 1 2 3]

#[0 1 2 3] * [2 2 2 2]
arr = arr * 2
print(arr)
print()
#[0 2 4 6]
