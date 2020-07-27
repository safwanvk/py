# Array in numpy

import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))
# Array is of type:  <class 'numpy.ndarray'>

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
# No. of dimensions:  2

# Printing shape of array
print("Shape of array: ", arr.shape)
# Shape of array:  (2, 3)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
# Size of array:  6

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
# Array stores elements of type:  int64

# Array creation

import numpy as np

# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype='float')
print("Array created using passed list:\n", a)
""" Array created using passed list:
 [[1. 2. 4.]
 [5. 8. 7.]] """

# Creating array from tuple
b = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", b)
""" Array created using passed tuple:
 [1 3 2] """

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print("\nAn array initialized with all zeros:\n", c)
""" An array initialized with all zeros:
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]] """

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype='complex')
print("\nAn array initialized with all 6s."
      "Array type is complex:\n", d)
""" An array initialized with all 6s.Array type is complex:
 [[6.+0.j 6.+0.j 6.+0.j]
 [6.+0.j 6.+0.j 6.+0.j]
 [6.+0.j 6.+0.j 6.+0.j]] """

# Create an array with random values
e = np.random.random((2, 2))
print("\nA random array:\n", e)
""" A random array:
 [[0.48546547 0.34577487] 
 [0.52720376 0.49145115]] """

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print("\nA sequential array with steps of 5:\n", f)
# A sequential array with steps of 5:
#  [ 0  5 10 15 20 25]

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print("\nA sequential array with 10 values between"
      "0 and 5:\n", g)
""" A sequential array with 10 values between0 and 5:
 [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
 3.33333333 3.88888889 4.44444444 5.        ] """

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print("\nOriginal array:\n", arr)
""" Original array:
 [[1 2 3 4]
 [5 2 4 2]
 [1 2 0 1]] """
print("Reshaped array:\n", newarr)
""" Reshaped array:
 [[[1 2 3]
  [4 5 2]]

 [[4 2 1]
  [2 0 1]]] """

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print("\nOriginal array:\n", arr)
""" Original array:
 [[1 2 3]
 [4 5 6]] """
print("Fattened array:\n", flarr)
""" Fattened array:
 [1 2 3 4 5 6] """

# Array slicing
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate"
      "columns(0 and 2):\n", temp)
""" Array with first 2 rows and alternatecolumns(0 and 2):
 [[-1.  0.]
 [ 4.  6.]] """

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),"
      "(3, 0):\n", temp)
""" Elements at indices (0, 3), (1, 2), (2, 1),(3, 0):
 [4. 6. 0. 3.] """

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print("\nElements greater than 0:\n", temp)
""" Elements greater than 0:
 [2.  4.  4.  6.  2.6 7.  8.  3.  4.  2. ] """

# Bais operations
# Operations on single array
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:", a + 1)
# Adding 1 to every element: [2 3 6 4]

# subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)
# Subtracting 3 from each element: [-2 -1  2  0]

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)
# Multiplying each element by 10: [10 20 50 30]

# square each element
print("Squaring each element:", a ** 2)
# Squaring each element: [ 1  4 25  9]

# modify existing array
a *= 2
print("Doubled each element of original array:", a)
# Squaring each element: [ 1  4 25  9]

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", a)
""" Original array:
 [[1 2 3]
 [3 4 5]
 [9 6 0]] """
print("Transpose of array:\n", a.T)
""" Transpose of array:
 [[1 3 9]
 [2 4 6]
 [3 5 0]] """

# unary operators
import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print("Largest element is:", arr.max())
# Largest element is: 9
print("Row-wise maximum elements:",
      arr.max(axis=1))
# Row-wise maximum elements: [6 7 9]

# minimum element of array
print("Column-wise minimum elements:",
      arr.min(axis=0))
# Column-wise minimum elements: [1 1 2]

# sum of array elements
print("Sum of all array elements:",
      arr.sum())
# Sum of all array elements: 38

# cumulative sum along each row
print("Cumulative sum along each row:\n",
      arr.cumsum(axis=1))
""" Cumulative sum along each row:
 [[ 1  6 12]
 [ 4 11 13]
 [ 3  4 13]] """

# Binary operator
import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])

# add arrays
print("Array sum:\n", a + b)
""" Array sum:
 [[5 5]
 [5 5]] """

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", a * b)
""" Array multiplication:
 [[4 6]
 [6 4]] """

# matrix multiplication
print("Matrix multiplication:\n", a.dot(b))
""" Matrix multiplication:
 [[ 8  5]
 [20 13]] """

# universal function
import numpy as np

# create an array of sine values
a = np.array([0, np.pi / 2, np.pi])
print("Sine values of array elements:", np.sin(a))
# Sine values of array elements: [0.0000000e+00 1.0000000e+00 1.2246468e-16]

# exponential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:", np.exp(a))
# Exponent of array elements: [ 1.          2.71828183  7.3890561  20.08553692]

# square root of array values
print("Square root of array elements:", np.sqrt(a))
# Square root of array elements: [0.         1.         1.41421356 1.73205081]

# sorting array
import numpy as np

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

# sorted array
print("Array elements in sorted order:\n",
      np.sort(a, axis=None))
""" Array elements in sorted order:
 [-1  0  1  2  3  4  4  5  6] """

# sort array row-wise
print("Row-wise sorted array:\n",
      np.sort(a, axis=1))
""" Row-wise sorted array:
 [[ 1  2  4]
 [ 3  4  6]
 [-1  0  5]] """

# specify sort algorithm
print("Column wise sort by applying merge-sort:\n",
      np.sort(a, axis=0, kind='mergesort'))
""" Column wise sort by applying merge-sort:
 [[ 0 -1  2]
 [ 1  4  5]
 [ 3  4  6]] """

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))
""" Array sorted by names:
 [(b'Aakash', 2009, 9. ) (b'Ajay', 2008, 8.7) (b'Hrithik', 2009, 8.5)
 (b'Pankaj', 2008, 7.9)] """

print("Array sorted by grauation year and then cgpa:\n",
      np.sort(arr, order=['grad_year', 'cgpa']))
""" Array sorted by grauation year and then cgpa:
 [(b'Pankaj', 2008, 7.9) (b'Ajay', 2008, 8.7) (b'Hrithik', 2009, 8.5)
 (b'Aakash', 2009, 9. )] """