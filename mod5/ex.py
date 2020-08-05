"""
What is binary data? Explain with examples.
Study the module pickle and explain how to use this module for reading and
writing a binary file.
"""

"""

    There are 8 bits in a byte
    Bits either consist of a 0 or a 1
    A byte can be interpreted in different ways, like binary octal or hexadecimal

Note: These are not character encodings, those come later. This is just a way to look at a set of 1’s and 0’s and see it in three different ways(or number systems).

Examples: 

Input : 10011011 
 
Output :
1001 1011 ---- 9B (in hex)
1001 1011 ---- 155 (in decimal)
1001 1011 ---- 233 (in octal)

This clearly shows a string of bits can be interpreted differently in different ways. We often use the hex representation of a byte instead of the binary one because it is shorter to write, this is just a representation and not an interpretation.
"""

# Reading and Writing to a Binary File
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

# raed 
f=open("binfile.bin","rb")
num=list(f.read())
print (num)
f.close()
# [5, 10, 15, 20, 25]

"""using pickle mdule """
import pickle
data = [1, 2, 3, 4]
f = open('pick.txt', 'wb')
pickle.dump(data, f)
f.close()

f = open('pick.txt', 'rb')
new_data = pickle.load(f)
print(new_data)
# [1, 2, 3, 4]

""" Write a program to read msword.doc format file and.docx format file and examine
the two formats and explain the differences."""

# # read .doc file
# import textract
# text = textract.process("/home/safwan/Desktop/xanthron/mod5/doc.doc") 

# read .docx file
import docx

doc = docx.Document("/home/safwan/Desktop/xanthron/mod5/Module 5.docx")
para = doc.paragraphs
print(len(para))
# 112

for i in para:
    print(i.text)

"""
1.DOC is the default extension of Word 2003 and older while DOCX is the default extension of Word 2007 and newer
2.Word 2003 and older cannot open DOCX files without the compatibility pack
3.DOCX is XML based while DOC is in a binary format
4.DOC is proprietary while DOCX is an open standard
5.DOCX can work with newer features while DOC cannot
"""

"""Escape Characters"""
"""
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert."""
# txt = "hai "Viki" "
# print(txt)
# # SyntaxError: invalid syntax

txt = "hai \"Viki\" "
print(txt)
# hai "Viki" 

# Other escape characters used in Python:
# Code 	Result 	
# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

""" Python Try Except """
"""The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks."""

""" Exception Handling """

""" When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:"""

try:
  print(x)
except:
  print("An exception occurred")
# An exception occurred

""" Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error: """

# print(x)
# # NameError: name 'x' is not defined

""" Many Exceptions """

"""You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:"""

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 
# Variable x is not defined

""" Else """

""" You can use the else keyword to define a block of code to be executed if no errors were raised: """
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 
#Hello
#Nothing went wrong

""" Finally """

"""The finally block, if specified, will be executed regardless if the try block raises an error or not."""
try:
  print(x)
except:
  print("Something went wrong")
finally: 

""" The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user. """

x = "hello"

if not type(x) is int:Traceback (most recent call last):
  File "/home/safwan/Desktop/xanthron/mod5/ex.py", line 189, in <module>
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed
  raise TypeError("Only integers are allowed")

"""Traceback (most recent call last):
  File "/home/safwan/Desktop/xanthron/mod5/ex.py", line 189, in <module>
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed """

