# Write a program to calculate the sum of n numbers.

n = int(input('enter limit'))
sum = 0
for i in range((n + 1)):
    sum = sum + i
print(sum)
""" enter limit5
15 """

# Write a program to find the biggest number from given three numbers.
num1 = int(input('enter first no'))
num2 = int(input('enter second no'))
num3 = int(input('enter third no'))
if num1 < num2:
    if num2 < num3:
        print('the biggest no is ' + str(num3))
    else:
        print('the biggest no is ' + str(num2))
elif num1 > num3:
    print('the biggest no is ' + str(num1))

""" enter first no43
enter second no2
enter third no1
the biggest no is 43 """

""" Write a Python program which accepts the user&#39;s first and last name
and print them in reverse order with a space between them """

first = input("enter first name")
last = input("enter last name")
print(last[::-1] + ' ' + first[::-1])

""" enter first nameajmal
enter last namesha
ahs lamja """

""" Write a Python program to test whether a number is within 100 or
1000 or 2000 """

no = int(input('enter a no'))
if no in range(2000):
    print('the no is within 2000')
if no in range(1000):
    print('the no is within 1000')
if no in range(100):
    print('the no is within 100')

""" enter a no50
the no is within 2000
the no is within 1000
the no is within 100 """

""" Write a Python program which accepts the radius of a circle from the
user and compute the area. """
r = int(input('enter radius'))
arae = 3.14 * r * r
print(arae)

""" enter radius5
78.5 """

""" Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum """
no1 = int(input('enter first no'))
no2 = int(input('enter second no'))
no3 = int(input('enter third no'))
sum = no1 + no2 + no3
if no1 == no2 == no3:
    sum1 = sum * 3
    print(sum1)
else:
    print(sum)
""" enter first no5
enter second no10
enter third no15
30 """

""" enter first no10
enter second no10
enter third no10
90 """

# Write a Python program to get the volume of a sphere with radius 6.
r = 6
volume = (4 / 3) * (3.14 * r * r * r)
print(volume)
# 904.3199999999999

""" Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn. """
i = int(input('enter no'))
res = i + (i * 10) + i + (i * 100) + (i * 10) + i
print(res)
""" enter no5
615 """

""" Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200 (both included). """

print([i for i in range(2000, 3200) if i % 5 != 0 and i % 7 == 0])


# [2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]

# Write a program which can compute the factorial of a given numbers.
def fact(num):
    factorial = 1
    for i in range(1, ((num) + 1)):
        factorial = factorial * i
    return factorial


num = int(input('enter no'))
res = fact(num)
print(res)

""" enter no5
120 """

"""  X = [[1,17,13],[4 ,15,26],[3 ,7,9]] and Y = [[25,81,12],[16,9,3],
[14,51,8]] ,
Write a program to add these two matrices. """
x = [[1, 17, 13], [4, 15, 26], [3, 7, 9]]
y = [[25, 81, 12], [16, 9, 3], [14, 51, 8]]
z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + y[i][j]
print(z)
# [[26, 98, 25], [20, 24, 29], [17, 58, 17]]

# How to convert a dictionary to list in python. Explain with examples.
dict = {'name': 'ajaml', 'age': 22}
list1 = list(dict.items())
print(list1)
# [('name', 'ajaml'), ('age', 22)]

list1 = []
for i in dict.items():
    list1.append(i)
print(list1)
# [('name', 'ajaml'), ('age', 22)]

""" A dictionary named student exists.
Explain the following
1. student.clear()
2. del student """

student = {'name': 'ajaml', 'age': 22}
# student.clear()
student.clear()
print(student)
# {}
# remove all the items of emp dictionary.

# del student
del student
print(student)


# NameError: name 'student' is not defined
# # delete the whole dictionary

#### function used #####

# Write a program to calculate the sum of n numbers.

def sum(n):
    sum = 0
    for i in range((n + 1)):
        sum = sum + i
    print(sum)


n = int(input('enter limit'))
sum(n)
""" enter limit5
15 """

# factorial
# Write a program which can compute the factorial of a given numbers.
num = int(input('enter no'))
factorial = 1
for i in range(1, ((num) + 1)):
    factorial = factorial * i
print(factorial)

""" enter no5
120 """



