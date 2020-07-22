# Set
a = {1, 2, 3, 5}
print(type(a))
# <class 'set'>
print(a)
# {1, 2, 3, 5}

# initialize with {}
a = {}
print(type(a))
# <class 'dict'>
a = set()
# <class 'set'>
# initilize with set
a = set()
print(type(a))
# <class 'set'>

# union()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# {'b', 1, 'c', 2, 3, 'a'}

# print letter
name = set(input('enter name'))
for i in name:
    print(i)
# safwan
# w
# a
# n
# f
# s

name = input('enter name')
for i in set(name):
    print(i)
# safwan
# w
# a
# n
# f
# s

# count letters
name = input('enter name')
for i in set(name):
    print(str(name.count(i)) + ' ' + i)
# aabb
# 2 a
# 2 b

# add
set1 = {'a', 'b', 'c'}
set1.add('d')
print(set1)
# {'a', 'c', 'b', 'd'}

# remove all elements
set1 = {'a', 'b', 'c'}
set1.clear()
print(set1)
# set()

# copy of the list
set1 = {'a', 'b', 'c'}
set2 = set1.copy()
print(set2)
# {'c', 'a', 'b'}

# diff b/w two or more set
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.difference(set1)
print(set3)
# {2, 3}
set4 = set1.difference(set2)
print(set4)
# {'b', 'c'}

# remove from the list and included in the specifired set
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set2.difference_update(set1)
print(set2)
# {2, 3}
set2 = {'a', 2, 3}
set1.difference_update(set2)
print(set1)
# {'c', 'b'}

# remove specified item
set1 = {'a', 'b', 'c'}
set1.discard('c')
print(set1)
# {'b', 'a'}

# intersection
# Return a set that contains the items that exist in both set set1, and set set2:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.intersection(set1)
print(set3)
# {'a'}
set3 = set1.intersection(set2)
print(set3)
# {'a'}

# Removes the items in this set that are not present in other, specified set(s)
# Remove the items that is not present in both set1, and set set2:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set1.intersection_update(set2)
print(set1)
# {'a'}

# Returns whether two sets have a intersection or not
# Return True if no items in set set1 is present in set ser1:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.isdisjoint(set1)
print(set3)
# False
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set2.isdisjoint(set1)
print(set3)
# True

# Returns whether another set contains this set or not
# Return True if all items set set2 are present in set set1:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.issubset(set1)
print(set3)
# false
set1 = {'a', 'b', 'c', 4}
set2 = {'a', 'b', 'c'}
set3 = set2.issubset(set1)
print(set3)
# True

# Returns whether this set contains another set or not
# Return True if all items set set1 are present in set set2:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.issuperset(set1)
print(set3)
# False
set1 = {'a', 'b', 'c'}
set2 = {'a', 'b', 'c', 4}
set3 = set2.issuperset(set1)
print(set3)
# True

# Removes an element from the set
set1 = {'a', 'b', 'c'}
set1.pop()
print(set1)
# {'c', 'b'}

# Removes the specified element
set1 = {'a', 'b', 'c'}
set1.remove('a')
print(set1)
# {'c', 'b'}

# Returns a set with the symmetric differences of two sets
# Return a set that contains all items from both sets, except items that are present in both sets:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set2.symmetric_difference(set1)
print(set3)
# {2, 3, 'b', 'c'}

# inserts the symmetric differences from this set and another
# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set1.symmetric_difference_update(set2)
print(set1)
# {2, 3, 'c', 'b'}

# Return a set containing the union of sets
# Return a set that contains all items from both sets, duplicates are excluded:
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set3 = set1.union(set2)
print(set3)
# {'c', 2, 'b', 'a', 3}

# Update the set with the union of this set and others
# Insert the items from set set2 into set set1
set1 = {'a', 'b', 'c'}
set2 = {'a', 2, 3}
set1.update(set2)
print(set1)
# {2, 3, 'b', 'c', 'a'}

# write a program to print the count of each character of given input string followed by the character
string = input('enter string')
for i in set(string):
    print(str(string.count(i)) + ' '+i)
# 3 M
# 4 A
# 3 L
# 2 I







