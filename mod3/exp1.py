# Python Dictionary

emp = {'name': 'arshad', 'age': 21}
print(type(emp))
# <class 'dict'>
print(emp)
# {'name': 'arshad', 'age': 21}

# access the data
emp = {'name': 'arshad', 'age': 21}
print(emp['name'])
# arshad
print(emp['age'])
# 21

# display all keys
emp = {'name': 'arshad', 'age': 21}
print(emp.keys())
# dict_keys(['name', 'age'])

# display all values
emp = {'name': 'arshad', 'age': 21}
print(emp.values())
# dict_values(['arshad', 21])

# returns items in a list format of (key, value) tuple pairs
emp = {'name': 'arshad', 'age': 21}
print(emp.items())
# dict_items([('name', 'arshad'), ('age', 21)])

# To Add a key-value pair to a dictionary
emp = {'name': 'arshad', 'age': 21}
emp['sex'] = 'M'
print(emp)
# {'name': 'arshad', 'age': 21, 'sex': 'M'}

# change already existing value in the dictionary
emp1 = {'name': 'arshad', 'age': 21, 'sex': 'M'}
emp1['age'] = 22
print(emp1)
# {'name': 'arshad', 'age': 22, 'sex': 'M'}

# To remove a key-value pair from a dictionary, del
emp1 = {'name': 'arshad', 'age': 21, 'sex': 'M'}
del emp1['sex']
print(emp1)
# {'name': 'arshad', 'age': 21}

# remove all the items of emp dictionary. dictionary.clear()
emp1 = {'name': 'arshad', 'age': 21, 'sex': 'M'}
emp1.clear()
print(emp1)
# {}

"""
# delete the whole dictionary. del dictionary
emp1 = {'name': 'arshad', 'age': 21, 'sex': 'M'}
del emp1
print(emp1)
# NameError: name 'emp1' is not defined """

# Local and Global variable
# global
n = 'I love India'


def myName():
    n = 'My name is MA Hadi'
    print(n)
    # My name is MA Hadi


myName()
print(n)
# I love India

n = 'I love India'


def myName():
    print(n)
    # I love India


myName()


# local
def myName():
    n = 'I love India'
    print(n)
    # I love India


myName()
print(n)
# NameError: name 'n' is not defined

# global keyword
n = 'I love India'


def myName():
    global n
    n = 'My name is MA Hadi'
    print(n)
    # My name is MA Hadi


myName()
print(n)
# My name is MA Hadi

# indentation 4 spaces
pwd = 'apple'
if pwd == 'apple':
    print('Logging on ...')
else:
    print('Incorrect password.')
    print('All done')
# Logging on ...

pwd = 'apple'
if pwd == 'apple':
    print('Logging on ...')
else:
    print('Incorrect password.')
print('All done')
""" Logging on ...
All done """

# comment use '#'
# comment here
"""
comment
here
"""

# Conditional Statements if, elif, else
x, y = 100, 900
if x < y:
    l = 'y is greater than x'
elif x == y:
    l = 'y is equal to x'
else:
    l = 'x is greater than y'
print(l)
# y is greater than x

# comprehension
x, y = 100, 900
l = 'x is less than y' if x < y else 'x is greater than or equal to y'
print(l)
# x is less than y

# loops
# while
x = 0
while x < 5:
    print(x)
    x = x + 1
""" 0
1
2
3
4 """

# for in range
# range(begin, end, step)
for i in range(5):
    print(i)
    """ 0
    1
    2
    3
    4 """

for i in range(5, 10):
    print(i)
    """ 5
    6
    7
    8
    9 """

for i in range(4, 10, 2):
    print(i)
    """ 4
    6
    8 """

for i in range(0, -10, -2):
    print(i)
    """ -2
    -4
    -6
    -8 """

# Loops over a collection(list)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in days:
    print(i)
    """ Mon
    Tue
    Wed
    Thu
    Fri
    Sat
    Sun """

""" Break and continue statements
break is used to exit from a specific loop under some conditions and
continue is used to continue the loop with out executing the code after
the continue statement under some conditions. """

for x in range(5, 10):
    if x == 7:
        break
    print(x)
    """ 5
    6 """

for x in range(5, 10):
    if x % 2 == 0:
        continue
    print(x)
    """ 5
    7
    9 """

# Using enumerate function
# get each member of the list(d) and the it’s index value(i).
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i, d in enumerate(days):
    print(i, d)


# function
# Function without any arguments
def func():
    print('Hello')


func()


# Hello

# Function with arguments
def func1(arg1, arg2):
    print(arg1, arg2)


func1(10, 11)


# 10 11

# Function that returns a value
def cube(x):
    return x * x * x


c = cube(3)
print(c)


# 27

# Function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


res = power(3)
print(res)
# 3

res = power(3, 5)
print(res)


# 243

# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


res = multi_add(12, 3, 23, 45)
print(res)
# 83
