# function

def main():
    print('inside the function')
print('outside the function')
# outside the function

if __name__ == "__main__":
    main()

"""outside the function
inside the function """

# Annoymous function
def sum(a, b):  
    return a + b
s = sum(1, 2)
print(s)
# 3
# This is function

x = lambda a, b:a + b
s = x(1, 2)
print(s)
# 3

def qe(a,b,c):
    return lambda x:a*x**2+b*x+c

f = qe(2,3,-5)
print(f(0))
print(f(1))
print(f(2))

"""
-5
0
9
"""

print(qe(2,3,-5)(0))
print(qe(2,3,-5)(1))
print(qe(2,3,-5)(2))
"""
-5
0
9
"""

# filter function
# negative
l1 = [-1, 0, 3, -2, 5]
x = list(filter(lambda x:x < 0, l1))
print(x) 
# [-1, -2]

# follow
n = [1,3,4,2,5]
x = list(filter(None, n))
print(x)
# [1, 3, 4, 2, 5]

"""If you want to filter missing data from a list of data, use filter as follows
name = [“”,”Hadi”,””,”Saji”,”Eza”,””,””,”Lajish”]"""

name = ['','Hadi','','Saji','Eza','','','Lajish']
x = list(filter(None, name))
print(x)
# ['Hadi', 'Saji', 'Eza', 'Lajish']

# map
def add(x, y):
    return x +  y
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]
x = list(map(add, l1, l2))
print(x)
# [3, 5, 7, 9, 11]

# using lambda
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]
x = list(map(lambda a,b: a + b, l1, l2))
print(x)
# [3, 5, 7, 9, 11]

# reduce
from functools import reduce
l = [1,2,3,4,5]
x = reduce(lambda a,b: a + b, l)
print(x)
# 15

# command line argument
import sys
for i in sys.argv:
    print(i)
""" exp.py | filename
hello | first argument
safwan | argument """

# Python JSON
# json to python 
import json

x = '{ "name": "seban", "age": 20, "city": "mlp" }'

y = json.loads(x)
print(y)
# {'name': 'seban', 'age': 20, 'city': 'mlp'}

# python to json
import json

x = { "name": "seban", "age": 20, "city": "mlp" }

y = json.dumps(x)
print(y)
# {"name": "seban", "age": 20, "city": "mlp"}

# file
import json
jf = open('exp.txt','r')
book = json.load(jf)
print(book)
jf.close()


