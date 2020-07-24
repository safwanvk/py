# normal function

def student(firstname, lastname, std):
    print(f'{firstname} {lastname} studied in {std} standerd')


student('zab', 'sha', 10)
# zab sha studied in 10 standerd

"""Positinal and Keyboard arguments
Positional arguments must be included in the correct order. Keyword arguments
are included with a keyword and equals sign. The order of these arguments matters when
they’re passed positionally. But when we use keyword/named arguments, it’s the name
that matters, not the position. """


# Positional args
def sum(a, b, c):
    sum = a - b / c
    print(sum)
    return


sum(1, 2, 3)
# 0.33333333333333337

sum(3, 2, 1)


# 1.0

# keyword args
def sum1(a, b, c):
    sum1 = a - b / c
    print(sum1)
    return


sum(a=1, b=2, c=3)
# 0.33333333333333337
sum(c=3, b=2, a=1)
# 0.33333333333333337

""" replacement of arguments given at the time
of function call or positional arguments. """


def student(firstname, lastname='sha', std='six'):
    print(firstname, lastname, 'studied in', std, 'standerd')


# 1 positional args
student('zab')
# zab sha studied in six standerd

# 3 positional args
student('zab', 'sha', 'nine')
# zab sha studied in nine standerd

# 2 positional args
student('zab', 'gates')
# zab gates studied in six standerd
student('john', 'seventh')


# john seventh studied in six standerd

# f-string
def student1(firstname, lastname='sha', std='six'):
    print(f'{firstname} {lastname} studied in {std} standerd')


# 1 positional args
student1('zab')
# zab sha studied in six standerd

# 3 positional args
student1('zab', 'sha', 'nine')
# zab sha studied in nine standerd

# 2 positional args
student1('zab', 'gates')
# zab gates studied in six standerd
student1('john', 'seventh')


# john seventh studied in six standerd

# default args with format function
def student(str_name='zab', str_site='www.google.com'):
    template = 'hai {name} welcome to {website} website'
    template = template.format(name=str_name, website=str_site)
    print(template)
    return


student()
# hai zab welcome to www.google.com website
student('sha', 'www.github.com')


# hai sha welcome to www.github.com website

# default args with f-string
def student(str_name='zab', str_site='www.google.com'):
    print(f'hai {str_name} welcome to {str_site} website')
    return


student()
# hai zab welcome to www.google.com website
student('sha', 'www.github.com')
# hai sha welcome to www.github.com website

# different formatting technique

print('{} {}'.format('hai', 'zab'))
# hai zab

print('{0} {1}'.format('hai', 'zab'))
# hai zab

print('{1} {0}'.format('hai', 'zab'))
# zab hai

print('{2} {0} {1}'.format('hai', 'zab', 'welcome'))
# welcome hai zab

""" print('{} {1}'.format('hai', 'zab'))
# ValueError: cannot switch from automatic field numbering to manual field specification """
