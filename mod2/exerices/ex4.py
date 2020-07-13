myList = [0, 6, 2, 7, 8, 9]
print(myList[1])
# 6
print(myList[0])
# 0

# print(myList[7])
# IndexError: list index out of range

print(myList[5])
# 9

# print(myList[4.0])
# TypeError: list indices must be integers or slices, not float

print(myList[-3])
# 7
print(myList[-1])
# 9
print(myList[2:6])
# [2, 7, 8, 9]
print(myList[4:5])
# 8
print(myList[6:1000])
# []
print(myList[2:4][1])
# 7
print(myList[0:3:2])
# [0, 2]
print(myList[1::3])
# [6, 8]
print(myList[::])
# [0, 6, 2, 7, 8, 9]
print(myList[2::2])
# [2, 8]
print(myList[::3])
# [0, 7]
print(myList[1::2])
# [6, 7, 9]
print(myList[::4])
# [0, 8]
print(myList[::2])
# [0, 2, 8]
print(myList[:])
# [0, 6, 2, 7, 8, 9]
print(myList[::-1][3:5])
# [2, 6]
print(myList[::-1])
# [9, 8, 7, 2, 6, 0]

# print(myList[3:5][4])
# IndexError: list index out of range

# print(myList[1:5][2:3][1])
# IndexError: list index out of range

print(myList[::1])
# [0, 6, 2, 7, 8, 9]

# print(myList[2::-2][-3])
# IndexError: list index out of range
