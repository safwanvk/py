# Reguler expression
# Select all numbers from a string
import re

s = ' My name is Devi. I am 22 years and 5 months old.My email is devi@gmail.com '
result = re.findall('[0-9]+',s)
print(result)
# ['22', '5']

result = re.findall('[0-9]',s)
print(result)
# ['2', '2', '5']

# 2. Extract only email id from a string

result = re.findall('\S+@\S+',s)
print(result)
# ['devi@gmail.com']

