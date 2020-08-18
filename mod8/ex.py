"""
Study re module of python and prepare a study material. """

# findall()
# The findall() function returns a list containing all matches

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# ['ai', 'ai']

# search()
""" The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned: """

import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.start())
# 3

# The split() function returns a list where the string has been split at each match:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# ['The', 'rain', 'in', 'Spain']

""" You can control the number of occurrences by specifying the maxsplit parameter: """
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# ['The', 'rain in Spain']

""" The sub() function replaces the matches with the text of your choice: """
import re

txt = "The rain in Spain"
x = re.sub("\s", "&", txt)
print(x)
# The&rain&in&Spain

""" You can control the number of replacements by specifying the count parameter: """
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# The9rain9in Spain

""" Match object
A Match Object is an object containing information about the search and the result. """
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
# <re.Match object; span=(5, 7), match='ai'>

""" .span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match """

# .span()
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# (12, 17)

# .string
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# The rain in Spain

# .search()
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Spain

# raw string
""" raw strings are raw string literals that treat backslash (\ ) as a literal character. For example, 
if we try to print a string with a “\n” inside, it will add one line break. But if we mark it as a raw string, 
it will simply print out the “\n” as a normal character. 
Python raw strings are useful for writing regular expressions and for using with SQL parsers.
Python raw strings are prefixed with ‘r’ or ‘R’. Prefix a string with ‘R’ or ‘r’ and it will be treated as a raw string. 
Let me show you an example : """

str = 'This is a \n normal string'
print(str)
"""
This is a
 normal string """

str = r'This is a \n normal string'
print(str)
# This is a \n normal string

str = R'This is a \n normal string'
print(str)
# This is a \n normal string

raw_str_one = R"This is a \t raw string with single quote"
raw_str_two = R"This is another \n raw string with double quotes"
raw_str_three = R"""This is a \t multiline raw string with
double triple quotes"""
raw_str_four = R'''This is a \t raw string with
  single triple quotes'''

print(raw_str_one)
print(raw_str_two)
print(raw_str_three)
print(raw_str_four)

"""
This is a \t raw string with single quote
This is another \n raw string with double quotes
This is a \t multiline raw string with
double triple quotes
This is a \t raw string with
  single triple quotes """

