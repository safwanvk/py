""" String Formatting
From processing input to printing messages on the screen, strings are a vital part of any programming language.
In Python, there are three ways of formatting strings: the original %s-method, the str.format(), and, since Python 3.6, f-strings. """

# %s
name = "sara"
day = "Tuesday"
print("Happy %s, %s. Welcome to Python!" % (day, name))

# Happy Tuesday, sara. Welcome to Python!

name = 'arun'
name1 = 'shankar'
print('hai %s %s' % (name, name1))
# hai arun shankar

# str.format()

print("Happy {}, {}. Welcome to Python!".format(day, name))
# Happy Tuesday, arun. Welcome to Python!

greeting = {'name': 'Monty', 'day': 'Tuesday'}
print("Happy {day}, {name}. Welcome to Python!".format(day=greeting['day'], name=greeting['name']))
# Happy Tuesday, Monty. Welcome to Python!
print("Happy {}, {}. Welcome to Python!".format(greeting['day'], greeting['name']))
# Happy Tuesday, Monty. Welcome to Python!

# f-string
name = "Monty"
day = "Tuesday"
print(f"Happy {day}, {name}. Welcome to Python!")
# Happy Tuesday, Monty. Welcome to Python!

# to print in multiple lines
str1 = """hlo
there
i'm here """
print(str1)
""" hlo
there
i'm here """

str_new = 'helo\nthere is new\nline'
print(str_new)
""" helo
there is new
line """

str_new1 = 'helo\nthere is not a new\nline'.replace('\n', '')
print(str_new1)
# helothere is not a newline

# print multiple line but in single line
str2 = """heloo.. \
this is \
not a new line """
print(str2)
# heloo.. this is not a new line

# fstring replace the name with
name = 'anu'
print(f"hi {name} i am xanthron")
# hi anu i am xanthron

lst = ['anu', 'shankar', 'majo']
for i in lst:
    print(f'helo {i}')
""" helo anu
helo shankar
helo majo """

# format function
print('{name} is a girl'.format(name='zoya'))

# \ may consider as escape character
str_web = 'https:\\google.com'
print(str_web)
# https:\google.com

str_web1 = 'https:\\\google.com'
print(str_web1)
# https:\\google.com





