# How To Remove Duplicates From A List in Python
dup = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# Print the unique `duplicates` list
print(list(set(dup)))
# [1, 2, 3, 5, 6, 7, 8]





# nested list comprehensions:

lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print([[x for x in sublist if x in lst1] for sublist in lst2])
# [[13, 32], [7, 13, 28], [1, 6]]

