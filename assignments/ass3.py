# one liner for….
# print list of 0 to 9 numbers
lst = [i for i in range(10)]

a = 2
b = 3
if a > b:
    print(a)
else:
    print(b)
# one liner if...

print(a) if (a > b) else print(b)

# find even or odd
lst_odd = []
lst_even = []
for i in range(50):
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)
print(lst_even, lst_odd)

# one liner for and if ...........
lst_odd = [i for i in range(50) if (i % 2 == 1)]
lst_even = [i for i in range(50) if (i % 2 == 0)]
print(lst_even, lst_odd)


# Find all the multiples of 3 and 5 which is less than 50
lst = [n for n in range(1, 50) if n % 3 == 0 and n % 5 == 0]
print(lst)
# [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48]

# create a dictionary in the format {i:i*i} where i from 1 to n for a limit n

print([{x: x*x} for x in range(1, (int(input('enter limit')) + 1))])
# 3
# [{1: 1}, {2: 4}, {3: 9}]

