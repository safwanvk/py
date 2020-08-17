# """ Write a single line program to sort the following list using lambda
# expression.
# List = ['Issac Newton','Issac Asimov','Orson Scott Card','Brain
# Mercurry','Vladimir Illich Lenin','Arthus C. Clarke']
# sort it by last name.
# The output must be as follows
# ['Issac Asimov', 'Orson Scott Card', 'Arthus C. Clarke',
# 'Vladimir Illich Lenin', 'Brain Mercurry', 'Issac Newton'] """

list = ['Issac Newton','Issac Asimov','Orson Scott Card','Brain Mercurry','Vladimir Illich Lenin','Arthus C. Clarke']
list.sort(key=lambda x:x.split(' ')[-1].lower())
print(list)
# ['Issac Asimov', 'Orson Scott Card', 'Arthus C. Clarke', 'Vladimir Illich Lenin', 'Brain Mercurry', 'Issac Newton']

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
import getopt 


def full_name(): 
	first_name = None
	last_name = None

	argv = sys.argv[1:] 

	try: 
		opts, args = getopt.getopt(argv, "f:l:") 
	
	except: 
		print("Error") 

	for opt, arg in opts: 
		if opt in ['-f']: 
			first_name = arg 
		elif opt in ['-l']: 
			last_name = arg 
	

	print(str(first_name) + ' ' + str(last_name)) 

full_name()	 

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

""" Study csv and json modules completely and write a short note about all its
methods with examples. """

# csv
""" CSV file is a type of plain text file that uses specific structuring to arrange tabular data. 
CSV is a common format for data interchange as it's compact, simple and general.
The standard format is defined by rows and columns data. Moreover, each row is terminated by a newline to begin the next row. 
Also within the row, each column is separated by a comma.
"""

# Read csv file
import csv
with open('data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)

""" ['\ufeffProgramming language', 'Designed by', 'Appeared', 'Extension']
['Python', 'Guido van Rossum', '1991', '.py']
['Java', 'James Gosling', '1995', '.java']
['C++', 'Bjarne Stroustrup', '1983', '.cpp'] """

# Read a CSV as a Dictionary
import csv

reader = csv.DictReader(open("data.csv"))
for raw in reader:
    print(raw)

""" {'\ufeffProgramming language': 'Python', 'Designed by': 'Guido van Rossum', 'Appeared': '1991', 'Extension': '.py'}
{'\ufeffProgramming language': 'Java', 'Designed by': 'James Gosling', 'Appeared': '1995', 'Extension': '.java'}
{'\ufeffProgramming language': 'C++', 'Designed by': 'Bjarne Stroustrup', 'Appeared': '1983', 'Extension': '.cpp'} """

# write CSV File
import csv

with open('X:\writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])


# Json

""" JSON is a standard format for data exchange, which is inspired by JavaScript. Generally, JSON is in string or text format. JSON stands for JavaScript Object Notation.

The syntax of JSON: JSON is written as key and value pair.

{
        "Key":  "Value",
        "Key":  "Value",
} 

JSON is very similar to Python dictionary. Python supports JSON, and it has an inbuilt library as a JSON. 

dumps() 	encoding to JSON objects
dump() 	encoded string writing on file
loads() 	Decode the JSON string
load() 	Decode while JSON file read  """

# dumps
import json

x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)

""" {
    "age": 45,
    "cars": [
        {
            "model": "Audi A1",
            "mpg": 15.1
        },
        {
            "model": "Zeep Compass",
            "mpg": 18.1
        }
    ],
    "children": [
        "Alice",
        "Bob"
    ],
    "married": true,
    "name": "Ken",
    "pets": [
        "Dog"
    ]
} """

# JSON file of the dictionary using the same function dump()

import json
x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# here we create new data_file.json file with write mode using file i/o operation 
with open('json_file.json', "w") as file_write:
  # write json data into file
  json.dump(x, file_write)

# JSON to Python (Decoding)
# loads()

import json  # json library imported
# json data string
person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj.get('person'))

""" {'person': {'name': 'Kenn', 'sex': 'male', 'age': 28}}
Type of dict_obj <class 'dict'>
Person...... {'name': 'Kenn', 'sex': 'male', 'age': 28} """

# Decoding JSON File or Parsing JSON file in Python
# load()

import json
#File I/O Open function for read data from JSON File
with open('json_file.json') as file_object:
        # store file data in object
        data = json.load(file_object)
print(data)

"""{'name': 'Ken', 'age': 45, 'married': True, 'children': ['Alice', 'Bob'], 'pets': ['Dog'], 
'cars': [{'model': 'Audi A1', 'mpg': 15.1}, {'model': 'Zeep Compass', 'mpg': 18.1}]} """
