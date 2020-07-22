# list
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

# string
str = 'image'
for i in str:
    print(i)
for i in 'image':
    print(i)

# integer
for i in range(6):
    print(i)

for i in range(0, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)

# dict
dict = {1: 'a', 2: 'b', 3: 'c'}
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)

user1 = {'name': 'muhsin', 'place': 'chatti', 'email': 'muhsin@gmail.com'}
user2 = {'name': 'arshad', 'place': 'mlp'}
list = [user1, user2]
print(list)
for i in list:
    if 'email' in i:
        print('name is' + ' ' + i['name'] + ' ' + 'place is' + ' ' + i['place'] + ' ' + 'email is' + ' ' + i['email'])
    else:
        print('name is' + ' ' + i['name'] + ' ' + 'place is' + ' ' + i['place'])


user1 = {'name': 'muhsin', 'place': 'chatti', 'age': 19}
user2 = {'name': 'arshad', 'place': 'mlp', 'age': 20}
user3 = {'name': 'zab', 'place': 'mlp', 'age': 21}
list = [user1, user2, user3]
print(list)
list1 = []
for i in list:
    if 'age' in i:
        if i['age'] > 20:
            list1.append(i['name'])
print(list1)

list = [1, 5, 3, 5, 7, 8, 2, 12]
list_odd = []
list_even = []

for i in list:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_odd)
print(list_even)

list = [1, 5, 3, 5, 7, 8, 2, 12]
list_odd = []
list_even = []
i = 0
while i < len(list):
    for i in list:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    i = i + 1
print(list_odd)
print(list_even)





