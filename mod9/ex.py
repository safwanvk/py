# assaign various names to a single funcion.

def fun1(num):
    print(num)

fun1("hai")
# hai

fun2 = fun1
fun2("hi")
# hi

# fun anther fuction as it's parameter

def add(x):
    return x + 1

def minus(x):
    return x - 1

def execute(fun, x):
    res = fun(x)
    print(res)

execute(add, 2)
# 3
execute(minus, 2)
# 1

# return another function too.

def called():
    def returned():
        print("Welcome!")
    return returned()
called()

# Welcome!

def decorated(func):
    def inner():
        print('Decorated with new function')
        func()
    return inner()
def myfunct():
    print('Before Decoration')

decorated(myfunct)
"""
Decorated with new function
Before Decoration
"""
def decorated(func):
    def inner():
        print('Decorated with new function')
        func()
    return inner()

@ decorated
def myfunct():
    print('Before Decoration')

"""
Decorated with new function
Before Decoration
"""

