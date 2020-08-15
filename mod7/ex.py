# """ Write a single line program to sort the following list using lambda
# expression.
# List = ['Issac Newton','Issac Asimov','Orson Scott Card','Brain
# Mercurry','Vladimir Illich Lenin','Arthus C. Clarke']
# sort it by last name.
# The output must be as follows
# ['Issac Asimov', 'Orson Scott Card', 'Arthus C. Clarke',
# 'Vladimir Illich Lenin', 'Brain Mercurry', 'Issac Newton'] """

# # list = ['Issac Newton','Issac Asimov','Orson Scott Card','Brain Mercurry','Vladimir Illich Lenin','Arthus C. Clarke']
# # list.sort(key=lambda x:x.split(' ')[-1].lower())
# # print(list)
# # ['Issac Asimov', 'Orson Scott Card', 'Arthus C. Clarke', 'Vladimir Illich Lenin', 'Brain Mercurry', 'Issac Newton']

# """ using getopt module and argparse module
# Expalin these two modules with examples. """

# """ The getopt module is a parser for command-line options based on the convention established by the Unix getopt() function. It is in general used for parsing an argument sequence such as sys.argv. In other words, this module helps scripts to parse command-line arguments in sys.argv. It works similar to the C getopt() function for parsing command-line parameters.
# Python getopt function
# The first function provided by this module is of the same name i.e. getopt(). Its primary functionality is to parse command-line options and parameter list. The syntax of the function is as below:
#     Syntax: getopt.getopt(args, options, [long_options])

#     Parameters:
#     args: List of arguments to be passed.
#     options: String of option letters that the script wants to recognize. Options that require an argument should be followed by a colon (:).
#     long_options: List of the string with the name of long options. Options that require arguments should be followed by an equal sign (=).

#     Return Type: Returns value consisting of two elements: the first is a list of (option, value) pairs. The second is the list of program arguments left after the option list was stripped. """

# import sys 
# import getopt 


# def full_name(): 
# 	first_name = None
# 	last_name = None

# 	argv = sys.argv[1:] 

# 	try: 
# 		opts, args = getopt.getopt(argv, "f:l:") 
	
# 	except: 
# 		print("Error") 

# 	for opt, arg in opts: 
# 		if opt in ['-f']: 
# 			first_name = arg 
# 		elif opt in ['-l']: 
# 			last_name = arg 
	

# 	print(str(first_name) + ' ' + str(last_name)) 

# full_name()	 

# """safwan@safwan-HP-EliteBook-840-G1:~/Desktop/xanthron/mod7$ python3 ex.py -f seban -l shahir
# seban shahir """

# argparse 
""" What is it?

Parser for command-line options, arguments and subcommands
Why use it?

The argparse module makes it easy to write user-friendly command-line interfaces.
How does it do that?

The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
Concept

When you run the “ls” command without any options, it will default displaying the contents of the current directory If you run “ls” on a different directory that you currently are in, you would type “ls directory_name”. 
The “directory_name” is a “positional argument”, which means that the program know what to do with the value.
To get more information about a file we can use the “-l” switch.

The “-l” is knowns as an “optional argument” If you want to display the help text of the ls command, you would type “ls –help” """

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)

""" safwan@safwan-HP-EliteBook-840-G1:~/Desktop/xanthron/mod7$ python3 ex.py -h
usage: ex.py [-h] square

positional arguments:
  square      display a square of a given number

optional arguments:
  -h, --help  show this help message and exit
safwan@safwan-HP-EliteBook-840-G1:~/Desktop/xanthron/mod7$ python3 ex.py 4
16 """
