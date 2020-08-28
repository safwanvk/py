def get_sum(a,b):
    if a == b:
        return b
    c = 0
    for n in range(min(a,b), max(a,b)+1):
        c += n
    return c

print(get_sum(1, 0))
# 1
print(get_sum(1, 2))
# 3
print(get_sum(0, 1))
# 1
print(get_sum(1, 1))
# 1
print(get_sum(-1, 0))
# -1
print(get_sum(-1, 2))
# 2

from math import sqrt
def find_next_square(sq):
	return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1

print(find_next_square(121))
# 144.0
print(find_next_square(625))
# 676.0
print(find_next_square(114))
# -1


def validate_pin(pin):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lenth = len(pin)
    i = 0
    if lenth == 4 or lenth == 6:
        while i < lenth:
            if pin[i] in numbers:
                   i += 1 
            else: return False
        return True 
    else:
        return False

print(validate_pin("1234"))
True
print(validate_pin("12345"))
False
print(validate_pin("a234"))
False

def middle_char(txt):
   return txt[(len(txt)-1)//2:(len(txt)+2)//2]

print(middle_char("tet"))

def get_middle(s):
    if(len(s) % 2 == 0):
        return "" + s[(int(len(s) / 2) - 1 )] + s[(int(len(s) / 2))]
    else:
        return s[(int(len(s)/2))]

print(get_middle('test'))
# es
print(get_middle('testing'))
# t
print(get_middle('middle'))
# dd
print(get_middle('a'))
# a



CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

print(from_morse('.... . -.--   .--- ..- -.. .'))
# HEYJUDE

def duplicate_count(text):
    new_text = text.lower()
    count = 0
    dictionary = {}
    for i in range(0,len(new_text)):
        dictionary[new_text[i]] = 0

    for key in dictionary:
        for i in range(0,len(new_text)):
            if(key == new_text[i]):
                dictionary[key] = dictionary[key] + 1

    for key in dictionary:
        if(dictionary[key] > 1):
            count = count + 1

    print(dictionary)
    return count

print(duplicate_count("indivisibility"))

def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

print(duplicate_count("abcde"))
# 0
print(duplicate_count("aabbcde"))
# 2
print(duplicate_count("aabBcde"))
# 2
print(duplicate_count("indivisibility"))
# 1
print(duplicate_count("indivisibilities"))
# 2
print(duplicate_count("aA11"))
# 2
print(duplicate_count("ABBA"))
# 2

def find_missing_letter(chars):
    missingChar = ''
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i])+1)

    return missingChar

print(find_missing_letter(['a','b','c','d','f']))
# e
print(find_missing_letter(['O','Q','R','S']))
# p



def order(sentence):
    words = [(int(l), w) for w in sentence.split() for l in w if l.isdigit()]
    words.sort(key=lambda t: t[0])
    return " ".join(t[1] for t in words)

print(order("is2 Thi1s T4est 3a"))

sentence = "is2 Thi1s T4est 3a"
new = " ".join(t[1] for t in sorted([(int(l), w) for w in sentence.split() for l in w if l.isdigit()], key=lambda t: t[0]))
print(new)
Thi1s is2 3a T4est

import re

final = ['' for i in range(1, 10)]
for w in input().split(' '):
    final[int(re.search(r"(\d)", w).group(0))-1] = w

print(' '.join(final))

def find_nb(m):
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                return n
            else:
                n = n + 1
                continue
        return -1

print(find_nb(1071225))
# 45
print(find_nb(91716553919377))
# -1

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

print(printer_error('aaabbbbhaijjjm'))
# 0/4
print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))
# 8/12



def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))



def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)



