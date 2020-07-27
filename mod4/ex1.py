# Sets in python

set1 = {1, 2, 3}
set2 = set([1, 2, 3])
print(set1)
# {1, 2, 3}
print(set2)
# {1, 2, 3}

# Adding element to the set
set1.add(4)
print(set1)
# {1, 2, 3, 4}

# A frozen set
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)
# frozenset({'g', 'e', 'f'})

# Adding element
people = {'Jay', 'Idrish', 'Archi'}
print(people)
# {'Archi', 'Idrish', 'Jay'}
# Add David to set
people.add('David')
print(people)
# {'Archi', 'Idrish', 'Jay', 'David'}

# Union
people = {'Jay', 'Idrish', 'Archil'}
dracula = {'Raju', 'Shankar'}
print(people, dracula)
# {'Archil', 'Idrish', 'Jay'} {'Raju', 'Shankar'}

# Union using union() function
population = people.union(dracula)
print(population)
# {'Archil', 'Raju', 'Jay', 'Shankar', 'Idrish'}

# Union using '|'
population = people | dracula
print(population)
# {'Idrish', 'Archil', 'Shankar', 'Jay', 'Raju'}

# Intersection
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)
print(set1, set2)
# {0, 1, 2, 3, 4} {3, 4, 5, 6, 7, 8}
# Intersection using intersection() function
set3 = set1.intersection(set2)
print(set3)
# {3, 4}

# Intersection using & operator
set3 = set1 & set2
print(set3)
# {3, 4}

# Difference
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)
print(set1, set2)
# Difference using difference() function
set3 = set1.difference(set2)
print(set3)
# {0, 1, 2}

# Difference using '-' operator
set3 = set1 - set2
print(set3)
# {0, 1, 2}

# Clear
set1 = {1, 2, 3, 4, 5, 6}
print(set1)
# {1, 2, 3, 4, 5, 6}
set1.clear()
print(set1)
# set()

# Python Arrays
# list
a = [1, 3.5, "Hello"]
print(a)
[1, 3.5, 'Hello']

# # array
# import array as arr
#
# a = arr.array(['d', [1, 3.5, "Hello"]])
# print(a)
""" Traceback (most recent call last):
  File "/home/safwan/xanthron/mod4/ex1.py", line 101, in <module>
    a = arr.array(['d', [1, 3.5, "Hello"]])
TypeError: array() argument 1 must be a unicode character, not list """

# Create array
import array as arr

a = arr.array('d', [1.1, 3.5, 4.5])
print(a)
# array('d', [1.1, 3.5, 4.5])

# Accessing element
import array as arr

a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

""" First element: 2
Second element: 4
Last element: 8 """

# Slicing
import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])  # beginning to end
""" array('i', [62, 5, 42])
array('i', [2, 5, 62])
array('i', [52, 48, 5])
array('i', [2, 5, 62, 5, 42, 52, 48, 5]) """

# Adding & changing
import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0
print(numbers)
# array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)
# array('i', [0, 2, 4, 6, 8, 10])

# Append and Extend
# append()
import array as arr

numbers = arr.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)
# array('i', [1, 2, 3, 4])

# extend()
numbers.extend([5, 6, 7])
print(numbers)
# array('i', [1, 2, 3, 4, 5, 6, 7])

# concatenate using '+' operator

import array as arr

odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])

numbers = arr.array('i')
numbers = odd + even

print(numbers)
# array('i', [1, 3, 5, 2, 4, 6])

# Removing

import array as arr

number = arr.array('i', [1, 2, 3, 3, 4])

# removing third element
del number[2]
print(number)
# array('i', [1, 2, 3, 4])

# # deleting entire array
# del number
# print(number)
""" Traceback (most recent call last):
  File "/home/safwan/xanthron/mod4/ex1.py", line 200, in <module>
    print(number)
NameError: name 'number' is not defined """

# remove()
import array as arr

numbers = arr.array('i', [10, 11, 12, 12, 13])

numbers.remove(12)
print(numbers)
# array('i', [10, 11, 12, 13])

print(numbers.pop(2))
# 12
print(numbers)
# array('i', [10, 11, 13])

# Matrix

A = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]

print("A =", A)
# A = [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]
print("A[1] =", A[1])  # 2nd row
# A[1] = [-5, 8, 9, 0]
print("A[1][2] =", A[1][2])  # 3rd element of 2nd row
A[1][2] = 9
print("A[0][-1] =", A[0][-1])  # Last element of 1st Row
# A[0][-1] = 12

column = [];
for row in A:
    column.append(row[2])

print("3rd column =", column)
# 3rd column = [5, 9, 11]

# Add two matrix


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
""" [17, 15, 4]
[10, 12, 9]
[11, 13, 18] """

# Matrix Transpose

X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
# [7, 5, 8]

# Multiplication two matrix
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
""" [114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23] """

# Square root calculation

import math

print(math.sqrt(4))
# 2.0

from math import sqrt, sin

x = 10
y = sqrt(x)
print(y)
# 3.1622776601683795


from math import *

print(pi)
# 3.141592653589793
print(factorial(6))
# 720

# OS Module

# os.name
import os

print(os.name)
# posix

# os.getcwd
import os

print(os.getcwd())
# /home/safwan/xanthron/mod4

# os.error
import os

try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
    print('Problem reading: ' + filename)
# Problem reading: GFG.txt

# os.popen()
import os

fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.
# Hello

# os.close()

# import os
#
# fd = "GFG.txt"
# file = open(fd, 'r')
# text = file.read()
# print(text)
# os.close(file)
""" Traceback (most recent call last):
  File "/home/safwan/xanthron/mod4/ex1.py", line 391, in <module>
    os.close(file)
TypeError: an integer is required (got type _io.TextIOWrapper) """

# os.rename()
import os

fd = "GFG.txt"
os.rename(fd, 'New.txt')
os.rename(fd, 'New.txt')
""" Traceback (most recent call last):
  File "/home/safwan/xanthron/mod4/ex1.py", line 404, in <module>
    os.rename(fd, 'New.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'GFG.txt' -> 'New.txt' """