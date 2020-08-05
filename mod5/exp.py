# # File Handling in python

# # Opening a file

# # mode-r readonly
# f = open('f1.txt', 'r')

# # mode-w writing
# f = open('f1.txt', 'w')

# # mode-a append
# f = open('f1.txt', 'a')  

# # mode-wb writing in binary
# f = open('f1.txt', 'wb') 

# # mode-rb reading in binary
# f = open('f1.txt', 'rb')

# # closing a file
# f.close()

# reading data
# read([member])
f = open('f1.txt', 'r')
var = f.read()
print(var)
f.close()
# File Handling in python

f = open('f1.txt', 'r')
var1 = f.read(6)
print(var1)
f.close()
#  File 

# readline()
f = open('f1.txt', 'r')
var1 = f.readline()
print(var1)
f.close()
#  File Handling in python

f = open('f1.txt', 'r')
var1 = f.readline(6)
print(var1)
f.close()
# File 

# readlines()
f = open('f1.txt', 'r')
var1 = f.readlines()
print(var1)
f.close()
# [' File Handling in python']

f = open('f1.txt', 'r')
var1 = f.readlines(6)
print(var1)
f.close()
# [' File Handling in python']

# appending in data
f = open('f1.txt', 'a')
f.write('new demmy data\n')
f.close()

# in 'w' mode
f = open('f1.txt', 'w')
f.write('new demmy data\n')
f.close()

# Reading data from a file using loop
f = open('f1.txt', 'r')
for i in f:
    print(i)
f.close()
# new demmy data



