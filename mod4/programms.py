"""
5. Write a program which finds all the words beginning with
“m” in a list and prints them out. It also should say how many
words it has found beginning with “m”. """

no = int(input('enter limit'))
list = [input('enter word:') for i in range(no)]
count = 0
print(list)
for i in list:
    if i[0] == 'm':
        print(f'{i} beginning with "m"')
        count = count + 1
print(f'{count} times found word beginning with "m"')

""" 
enter limit5
enter word:abu
enter word:maji
enter word:mike
enter word:shankar
enter word:mji
['abu', 'maji', 'mike', 'shankar', 'mji']
maji beginning with "m"
mike beginning with "m"
mji beginning with "m"
3 times found word beginning with "m" """

"""
6. Write a program to implement the following sorting
algorithms.
a. bubble sort
b. selection sort
c. Merge sort
d. insertion sort """

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input('enter limit of Array'))
arr = [input('enter element:') for i in range(n)]
bubble_sort(arr)
print('Sorted Array:')
for i in range(len(arr)):
    print(arr[i])
"""
enter limit of Array5
enter element:64
enter element:34
enter element:25
enter element:12
enter element:22
Sorted Array:
12
22
25 
34
64 """

# Selection Sort

n = int(input('enter limit of Array'))
arr = [input('enter element:') for i in range(n)]
for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print('Sorted Array:')
for i in range(len(arr)):
    print(arr[i])

"""
enter limit of Array5
enter element:65
enter element:34
enter element:25
enter element:12
enter element:22
Sorted Array:
12
22
25
34
65 """

# Merge sort
import numpy as np
n = int(input('enter limit of Array'))
a = np.array([input('enter element:') for i in range(n)])
print("merge-sort:\n",
      np.sort(a, kind='mergesort'))


# Insertion Sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


n = int(input('enter limit of Array'))
arr = [input('enter element:') for i in range(n)]
insertionSort(arr)
print('Sorted Array:')
for i in range(len(arr)):
    print(arr[i])

""" 
enter limit of Array3
enter element:23
enter element:1
enter element:67
Sorted Array:
1
23
67 """

""" 7.Write a Python program to concatenate 3 dictionaries to create
a new one. """

dict1 = {'name': 'seban'}
dict2 = {'cls': 10}
dict3 = {'age': 16}
dict4 = {}
[dict4.update(i) for i in (dict1, dict2, dict3)]
print(dict4)
# {'name': 'seban', 'cls': 10, 'age': 16}

""" 8.Write a Python program to sum all the items in a dictionary."""

dict1 = {'a': 100, 'b': 200, 'c': 300}
sum = 0
for i in dict1:
    sum = sum + dict1[i]
print(sum)
# 600