# Write a program using decorators with multiple parameters.

def div_decarator(func):
    def inner(x, y):
        print('dividing ', x, 'and', y)
        if y == 0:
            print('Oops! Division by zero is illegal!')
            return
        return func(x, y)
    return inner

@div_decarator
def divide(a, b):
    return a / b

print(divide(20, 2))
print(divide(20, 0))

"""
dividing  20 and 2
10.0
dividing  20 and 0
Oop! Division by zero is illegal!
None
"""

# Write a program using multiple decorator to add functionalities to and original function

def upper_decarator(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def split_decarator(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_decarator
@upper_decarator
def dec():
    return "Welcome to Xanthron"

print(dec())
# ['WELCOME', 'TO', 'XANTHRON']
