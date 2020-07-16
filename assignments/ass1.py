# list vs tuple
import copy
from random import choice, randrange

no_list = [1, 2, 3, 4]
print(type(no_list))
# <class 'list'>

no_tuple = (1, 2, 3, 4)
print(type(no_tuple))
# <class 'tuple'>

no_list.append(5)
print(no_list)
# [1, 2, 3, 4, 5]

# no_tuple.append(7)
# AttributeError: 'tuple' object has no attribute 'append'

no_list1 = [7, 8, 9]
no_list.extend(no_list1)
print(no_list)
# [1, 2, 3, 4, 5, 7, 8, 9]

""" no_tuple1 = (7, 8, 9)
no_tuple.extend(no_tuple1)
print(no_tuple)
AttributeError: 'tuple' object has no attribute 'extend' """

no_list.remove(5)
print(no_list)
# [1, 2, 3, 4, 7, 8, 9]

""" no_tuple.remove(3)
print(no_tuple)
AttributeError: 'tuple' object has no attribute 'remove' """

no_list.pop()
print(no_list)
# [1, 2, 3, 4, 7, 8]

""" no_tuple.pop()
print(no_tuple)
AttributeError: 'tuple' object has no attribute 'pop' """

# Lists Versus Dictionaries

no_dict = {'no': 1, 'name': 'safwan'}
print(type(no_dict))
# <class 'dict'>
print(no_dict['name'])
# safwan

# Lists Versus Sets

no_set = {1, 2, 3, 4}
print(type(no_set))
# <class 'set'>

no_list1 = [{'no': 1, 'name': 'safwan'}, 1]
print(no_list1)
[{'no': 1, 'name': 'safwan'}, 1]

"""
no_set1 = {{'no': 1, 'name': 'safwan'}, 1}
print(no_set1)
TypeError: unhashable type: 'dict'
"""

no_list1 = [1, 1]
print(no_list1)
[1, 1]

no_dict1 = {1, 1}
print(no_dict1)
# {1} Duplicates are not allowed in sets

# select element

list = ['amal', 'sha', 'shaf']
list1 = list[0]
print(list1)
# amal

list = ['amal', 'sha', 'shaf']
list1 = list[-1]
list2 = list[-2]
print(list1)
print(list2)
# shaf
# sha

list = 'amal'
list1 = list[2:]
print(list1)
# al

list = 'amalgosh'
list1 = list[0:8]
print(list1)
# amalgosh

list = 'amalgosh'
list1 = list[4:]
print(list1)
# gosh

list = 'amalgosh'
list1 = list[:8]
print(list1)
# amagosh

list = 'amalgosh'
list1 = list[:]
print(list1)
# amalgosh

list = 'amalgosh'
list1 = list[0:8:2]
print(list1)
# aags

from random import choice

list = ['amal', 'sha', 'shaf']
print(choice(list))
# amal

# How To Convert A List To A String
# List of Strings to a String
list_string = ['amal', 'sha', 'shaf']
str_strng = ''.join(list_string)
print(str_strng)
# List of integers to a String
list_int = [1, 2, 3]
str_int = ''.join(str(i) for i in list_int)
print(str_int)

# How To Convert A List To A Tuple
list_string = ['lama', 'sha', 'zab']
tuple_string = tuple(list_string)
print(type(tuple_string))
print(tuple_string)
# <class 'tuple'>
# ('lama', 'sha', 'zab')

# How To Convert Your List To A Set In Python
list_string = ['lama', 'sha', 'zab']
list_set = set(list_string)
print(type(list_set))
print(list_set)

# How To Convert Lists To A Dictionaries
list_user = ['name', 'amal', 'age', 20]
list_dict = dict(zip(list_user[0::2], list_user[1::2]))
print(type(list_dict))
print(list_dict)
# <class 'dict'>
# {'name': 'amal', 'age': 20}

# large list
list_user = ['name', 'amal', 'age', 20, 'place']
# Create a list iterator object
i = iter(list_user)
# Zip and create a dictionary
print(dict(zip(i, i)))
# {'name': 'amal', 'age': 20}

# How To Determine The Size Of Your List in Python
# list
len_list = ['amal', 'sha', 'xab']
print(len(len_list))
# 3

# dictionaries
len_dic = {'name': 'amal', 'age': 20, 'place': 'mlp'}
print(len(list_dict))
# 2

# set
len_set = ('amal', 'sha', 'xab', 'zab')
print(len(len_set))
# 4

# string
len_string = 'amalsha'
print(len(len_string))
# 7

# Append 4 to list
list = [1, 2, 3]
list.append(4)
print(list)
# [1, 2, 3, 4]

# Extend long_list with list
list = [1, 2, 3, 4]
long_list = [5, 6, 7]
long_list.extend(list)
print(long_list)
# [5, 6, 7, 1, 2, 3, 4]

# How To Concatenate Lists in Python
list1 = ['amal', 'sha']
list2 = ['zab', 'sha']
list3 = list1 + list2
print(list3)
# ['amal', 'sha', 'zab', 'sha']

# How To Sort a List in Python
# sort method
list = [1, 5, 7, 2, 9]
list.sort()
print(list)
# [1, 2, 5, 7, 9]

# sorted function
list = [1, 5, 7, 2, 9]
list_sort = sorted(list)
print(list_sort)
# [1, 2, 5, 7, 9]

# How To Clone Or Copy A List

# newList = oldList[:]
oldlist = ['amal', 'shaf', 'xab']
print(oldlist)
# ['amal', 'shaf', 'xab']
newlist = oldlist[:]
print(newlist)
# ['amal', 'shaf', 'xab']

"""
# list()
oldList = [1, 2, 3]
newList = list(oldList)
print(newList)
# [1, 2, 3]
"""

# copy library
import copy

oldList = ['amal', 'shaf']
print(oldList)
# ['amal', 'shaf']
newList = copy.copy(oldList)
print(newList)
# ['amal', 'shaf']

# copy.deepcopy()
oldList = ['shaf', 'zab', 'zax']
print(oldList)
# ['shaf', 'zab', 'zax']
newList = copy.deepcopy(oldList)
print(newList)
# ['shaf', 'zab', 'zax']

# deepcopy()
objectList = ['a', 'b', ['ab', 'ba']]
copiedList = objectList[:]
copiedList[0] = 'c'
copiedList[2][1] = 'd'
print(objectList)
# ['a', 'b', ['ab', 'd']]

# List Comprehension
print([x ** 2 for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension using if
print([x ** 2 for x in range(10) if x % 2 == 0])
# [0, 4, 16, 36, 64]

# lamda
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(lambda x: x * x)(x) for x in myList])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x * x
print([f(x) for x in range(10)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# How To Count Occurrences Of A List Item

# Counting the occurrences of one item in a list
list = ['amal', 'amal', 'zab']
print(list.count('amal'))
# 2

# Counting all items in a list with count()
list = ['amal', 'amal', 'zab']
print([(x, list.count(x)) for x in set(list)])
# [('zab', 1), ('amal', 2)]

# Counting all list items with Counter()
from collections import Counter

list = ['amal', 'amal', 'zab']
print(Counter(list))
# Counter({'amal': 2, 'zab': 1})


# How To Split A Python List Into Evenly Sized Chunks

""" # Your list `x`
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Split `x` up in chunks of 3
y = zip(*[iter(x)]*3)
# Use `list()` to print the result of `zip()`
print(list(y))
# [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
"""

# Set up your list and chunk size
list = range(0, 50)
chunk = 5
# Split up your list into chunks
print([list[i:i + chunk] for i in range(0, len(list), chunk)])
# [range(0, 5), range(5, 10), range(10, 15), range(15, 20), range(20, 25), range(25, 30), range(30, 35), range(35, 40), range(40, 45), range(45, 50)]


# How To Loop over A List in Python

mylist = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
for x in mylist:
    print(x)
"""
[1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10]
"""

# enumerate

myList = [3, 4, 5, 6]
for i, val in enumerate(myList):
    print(i, val)
"""
0 3
1 4
2 5
3 6
"""

# list comprehension
myList = [3, 4, 5, 6]
print([x for x in myList])
# [3, 4, 5, 6]

#  How To Create Flat Lists Out Of Lists

list = [[1, 2], [3, 4], [5, 6]]
print(sum(list, []))
# [1, 2, 3, 4, 5, 6]

# How To Get An Intersection Of Two Python Lists
"""
# List Intersection Using List Comprehension
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print([list(filter(lambda x: x in lst1, sublist)) for sublist in lst2])
# [[13, 32], [7, 13, 28], [1, 6]]
"""
"""
# nested list comprehensions:

lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print([[x for x in sublist if x in lst1] for sublist in lst2])
# [[13, 32], [7, 13, 28], [1, 6]]
"""


# Intersecting Lists With set()
# set
list_set = [1, 2]
list_set1 = [3, 2]
print(list(set(list_set) & set(list_set1)))
# [2]

# Use `intersection()`
list_intersection = [1, 2]
list_intersection1 = [2, 3]
print(list(set(list_intersection).intersection(list_intersection1)))
[2]


# How To Remove Duplicates From A List in Python
dup = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# Print the unique `duplicates` list

print(list(set(dup)))