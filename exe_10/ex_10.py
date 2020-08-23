
import re
string = input('Enter sentence to remove vowels:')
print(re.sub("[aeiouAEIOU]","",string))

"""
Enter sentence to remove vowels:WELCOME to Xanthron
WLCM t Xnthrn
"""

a=[]
n=int(input('Enter number of elements:'))
for i in range(0,n):
    b=int(input('Enter element:'))
    a.append(b)
k=0
num=int(input('Enter the number to be counted:'))
for j in a:
    if j == num:
        k=k+1
print(f'{num} has occured {k} times')

"""
Enter number of elements:5
Enter element:1
Enter element:3
Enter element:3
Enter element:2
Enter element:5
Enter the number to be counted:3
3 has occured 2 times
"""

str = input('Enter string containing numbers:')
num_list = list(map(int, str.split()))
print(f'Highest No:{max(num_list)} Lowest No:{min(num_list)}')

"""
Enter string containing numbers:15 3 22 0
Highest No:22 Lowest No:0
"""

def words(sentence):
    arr = sentence.split()
    ans = []
    [ans.append(i[::-1]) if len(i) >= 5 else ans.append(i) for i in arr]
    return ' '.join(ans)

sentence = input('Enter sentence:')
print(words(sentence))

"""
Enter sentence:Welcome to xanthron
emocleW to norhtnax
"""

def longest_string(string, k):
    if (len(string) == 0 or k <= 0) or len(string) < k:
        return "invalid"
    lst = [''.join(string[i:i+k]) for i in range(len(string))]
    return max(lst, key= lambda x: len(x))

print(longest_string(['zone', 'abigail', 'theta', 'form', 'libe', 'zas', 'theta', 'abigail'], 2))

# abigailtheta


def  count(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

i = int(input('Enter number:'))
print(count(i))

"""
Enter number:1234
5
"""

def check(data):
    res = []
    [res.append('Senior') if i[0] >= 55 and i[1] > 7 else res.append('Open') for i in data]
    return res

result = check([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])
print(result)

# ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']

def find(no):
    evens = []
    odds = []
    for i in no:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    print('Evens:', evens)
    print('Odds:', odds)
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]

print(find([2, 4, 0, 100, 4, 11, 2602, 36]))

"""
Evens: [2, 4, 0, 100, 4, 2602, 36]
Odds: [11]
11
"""

def isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

print(isogram('Dermatoglyphics'))
print(isogram('aba'))
print(isogram('moOse'))

"""
True
False
False
"""

def pow(n, p):
    if n > 0 and p > 0
    digits = (int(i) for i in str(n))
    result = 0
    for x in digits:
        result += x ** p
        p += 1

    if result % n:
        return -1
    else:
        return result // n

print(pow(89, 1))
print(pow(695, 2))
print(pow(46288, 3))

"""
1
2
51
"""


import math

def power(n,p):
    lhs = sum(int(d) ** q for q, d in enumerate(str(n), p))
    if lhs % n == 0:
        return lhs // n
    else:
        print("no k such that {} = {}*k".format(lhs, n))

print(power(46288, 3))
print(power(89, 1))
print(power(695, 2))

"""
51
1
2
"""