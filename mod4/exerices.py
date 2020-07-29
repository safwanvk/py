""" 1. How to get the below output while giving the input as
[Apple, Boy, Cat, Dog]
output: Boy, Cat, Dog(should be a single string) """

l = int(input('enter limit'))
list1 = [input('enter word') for i in range(l)]
list2 = []
for i in list1:
    if len(i) == 3:
        list2.append(i)
list3 = ', '.join(list2)
print(list3)

""" enter limit3
enter wordabhii
enter wordabi
enter wordabi
abi, abi """

""" 2. Find number in list which is not occurring multiple times """
list1 = []
l = int(input('enter limit'))
for i in range(l):
    no = input('enter no')
    list1.append(no)
print([i for i in list1 if list1.count(i) == 1])

""" enter limit5
enter no1
enter no2
enter no2
enter no4
enter no4
['1'] """


""" 3. Write program to count the occurrence of each word in given sentence? """
snt = input('enter sentence:')
word = snt.split(' ')
for i in set(word):
    print(str(word.count(i)) + ' ' + i)

""" enter sentence:hai hai zayn
1 zayn
2 hai """

""" 4. Program to accept a comma separated sequence of words as input and prints the
unique words in sorted form(alphanumerically) """

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

""" 5. code to get a list of words and returns the length of longest one """
n = int(input('enter limit'))
words = [input('enter word:') for i in range(n)]
max_len = []
for i in words:
    max_len.append((len(i), i))
max_len.sort()
print('the longest word length is {a} and word is {b}'.format(a=max_len[-1][0], b=max_len[-1][1]))

##### or #####
string = input('enter word:')
words = [word for word in string.split(" ")]
max_len = []
for i in words:
    max_len.append((len(i), i))
max_len.sort()
print('the longest word length is {a} and word is {b}'.format(a=max_len[-1][0], b=max_len[-1][1]))


""" enter limit5
enter word:abhi
enter word:shankar
enter word:madhav
enter word:ali
enter word:shake
the longest word length is 7 and word is shankar"""

""" 6. Code to print as …
Input: INDIA
Output: ANDII """

word = list(input('enter word:'))
temp = word[0]
word[0] = word[-1]
word[-1] = temp
str = ''.join(word)
print(str)

""" enter word:india
andii """

""" 7. Code to print ‘Yes’ if the index of two equal sized strings contains the same letter
else print ‘No’ """

str1 = input('enter string:')
str2 = input('enter another string:')
index = int(input('enter index:'))
if len(str1) == len(str2):
    if str1[index + 1] == str2[index + 1]:
        print('yes')
    else:
        print('no')
else:
    print('enter equal index values')

""" enter string:apu
enter another string:abu
enter index:1
yes """

""" 8. c. """

""" 8. Write code to prompt user to enter integer until they entered ‘done’ and print the
maximum and minimum among them. """

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None or largest < num: largest = num
        if smallest is None or smallest > num: smallest = num
    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)

""" Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: done
Maximum is 3
Minimum is 1 """

""" 9. Two teachers, teacher A and teacher B rated students separately and some of the
students are rated by both. The principal want to get the students who are rated by
both.
Input following things:
First line: No. of students rated by teacher A
Second line: student’s roll number, who are rated by A
Third line : No. of students rated by teacher B
Fourth line: student’s roll number, who are rated by B """

no_a = int(input('enter no of students rated by teacher A: '))
roll_a = [(input('student’s roll number, who are rated by A: ')) for i in range(no_a)]
no_b = int(input('enter no of students rated by teacher B: '))
roll_b = [(input('student’s roll number, who are rated by B: ')) for i in range(no_b)]
reg = []
for i in roll_a:
    if i in roll_b:
        reg.append(i)
print(reg)

""" enter no of students rated by teacher A: 2
student’s roll number, who are rated by A: ab001
student’s roll number, who are rated by A: ab005
enter no of students rated by teacher B: 2
student’s roll number, who are rated by B: ab005
student’s roll number, who are rated by B: ab002
['ab005'] """

""" 10. Check whether a string is keyword or not """

import keyword

keyword_list = keyword.kwlist
k = input('enter string: ')
if k in keyword_list:
    print('the string is keyword')
else:
    print('the string is not keyword')

""" enter string: if
the string is keyword 
enter string: abu
the string is not keyword """





