# modules

# command import
import math
import sys
import re

# To get the list of builtin modules do the following
import sys

print(sys.builtin_module_names)

# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree',
# '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random',
# '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct',
# '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins',
# 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat',
# 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')

# math
import math
# sqrt()

x = 10
y = math.sqrt(x)
print(y)
# 3.1622776601683795

# ceil()
x = 10.999
y = math.ceil(x)
print(y)
# 11

# sin()
x = 10
y = math.sin(x)
print(y)
# -0.5440211108893698

# tan()
x = 10
y = math.tan(x)
print(y)
# 0.6483608274590866

# factorial()
x = 10
y = math.factorial(x)
print(y)
# 3628800


# trunc()
x = 10
y = math.trunc(x)
print(y)
# 10

# floor()
x = 10.999
y = math.floor(x)
print(y)
# 10

# exp()
x = 10.999
y = math.exp(x)
print(y)
# 59814.297500576984

# log()
x = 10
y = math.log(x)
print(y)
# 2.302585092994046

# pow()
x = 10
y = math.pow(x, 2)
print(y)
# 100.0

# cos
x = 10
y = math.cos(x)
print(y)
# -0.8390715290764524

# asin()
x = -1
y = math.asin(x)
print(y)
# -1.5707963267948966

# radians()
x = 10
y = math.radians(x)
print(y)
# 0.17453292519943295

# gamma()
x = 10
y = math.gamma(x)
print(y)
# 362880.0

# pi
x = 10
y = math.pi
print(y)
# 3.141592653589793

# e
x = 10
y = math.e
print(y)
# 2.718281828459045

# import a specific function
from math import sin, sqrt
x = 10
y = sin(x)
print(y)
# -0.5440211108893698

x = 10
y = sqrt(x)
print(y)
# 3.1622776601683795

""" 
# packages
import pack.md
from pack import md """










