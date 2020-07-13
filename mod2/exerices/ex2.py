tuple = ("university", [5, 4, 6], (3, 2, 1))

# tuple[1][1] = 20
# tuple[2][2] = 0
# print(tuple)
# TypeError: 'tuple' object does not support item assignment

tuple = ("university", [5, 4, 6], [3, 2, 1])
tuple[1][1] = 20
tuple[2][2] = 0
print(tuple)
# ('university', [5, 20, 6], [3, 2, 0])
