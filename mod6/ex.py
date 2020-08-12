""" 1. What is garbage collection in python? """
""" Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. 
The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.
Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. 
An object's reference count changes as the number of aliases that point to it changes.
An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). 
The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. 
When an object's reference count reaches zero, Python collects it automatically.
You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space. 
But a class can implement the special method __del__(), called a destructor, that is invoked when the instance is about to be destroyed. 
This method might be used to clean up any non memory resources used by an instance. """

"""2. Explain with example the following python function
a. issubclass()
b. isinstance()
c. super() """

# issubclass()
""" Python issubclass() is a built-in function that returns true if a class supplied as the first argument is 
the subclass of another class supplied as the second argument, else it returns false. """

class Car:
    pass

class Maruti(Car):
    pass

print(issubclass(Maruti, Car))
# True
print(issubclass(Car, Maruti))
# False

# isinstance()
""" The isinstance() function checks if the object argument is an instance or subclass of classinfo class argument. """
marks = 100
result = isinstance(marks, int)
if result :
  print("Yes! given variable is an instance of type int")
else:
  print("No! given variable is not an instance of type int")
# Yes! given variable is an instance of type int
# No! given variable is not an instance of type int if marks = 'zab'

# super()
""" The super() function is used to give access to methods and properties of a parent or sibling class.
The super() function returns an object that represents the parent class. """

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()
# Hello, and welcome!

""" 3. Explain multiple inheritance and multilevel inheritance with proper examples in python. """
""" Multiple Inheritance
When a child class inherits from multiple parent classes, it is called multiple inheritance."""

class Base1(object): 
    def __init__(self): 
        self.str1 = "Hai"
        print("Base1") 
  
class Base2(object): 
    def __init__(self): 
        self.str2 = "Welcome"        
        print("Base2") 
  
class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print("Derived") 
          
    def printStrs(self): 
        print(self.str1, self.str2) 
         
  
ob = Derived() 
ob.printStrs() 
# Hai Welcome

""" Multilevel inheritance
When we have a child and grandchild relationship """


# A Python program to demonstrate inheritance  
  
# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is  
# equivalent to "class Person(object)" 
class Base(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
  
  
# Inherited or Sub class (Note Person in bracket) 
class Child(Base): 
      
    # Constructor 
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self.age = age 
  
    # To get name 
    def getAge(self): 
        return self.age 
  
# Inherited or Sub class (Note Person in bracket) 
class GrandChild(Child): 
      
    # Constructor 
    def __init__(self, name, age, address): 
        Child.__init__(self, name, age) 
        self.address = address 
  
    # To get address 
    def getAddress(self): 
        return self.address         
  
# Driver code 
g = GrandChild("zab", 23, "mlp")   
print(g.getName(), g.getAge(), g.getAddress()) 
# zab 23 mlp


""" 4. Write a python program to create a new table with following structure.
Database name: xanthron
Table name : country """
""" COUNTRY_ID
| varchar(2)
| YES |
| NULL
|
|
| COUNTRY_NAME | varchar(40)
| YES |sudo /opt/lampp/uninstall
| NULL
|
|
| REGION_ID
| decimal(10,0) | YES |
| NULL """

# # Create Database
# import MySQLdb
# db = MySQLdb.connect(
# host="127.0.0.1",
# user="root",
# password="",)

# cur = db.cursor()
# cur.execute("CREATE DATABASE xanthron")

# # Craete Table
# import MySQLdb
# db = MySQLdb.connect(
# host="127.0.0.1",
# user="root",
# password="",
# db='xanthron',)

# cur = db.cursor()
# cur.execute("CREATE TABLE country (COUNTRY_ID varchar(2) NULL,COUNTRY_NAME varchar(40) NULL,REGION_ID decimal(10,0) NULL)")

# """ 5. Write a python program to insert records to the country table. """

# sql = "INSERT INTO country (COUNTRY_ID,COUNTRY_NAME,REGION_ID) VALUES (%s,%s,%s)"
# val = ("c1","kolkatta",101)
# cur.execute(sql, val)

# db.commit()

# print(cur.rowcount, "record inserted.")
# # 1 record inserted

# """ 6. Write a program to read all the records from the country table and display it."""

# cur.execute("SELECT * FROM country")
# for row in cur.fetchall() :
#     print(row[0], " ", row[1], " ", row[2])
# # c1   kolkatta   101

# """7. Write a class Company with following attributes.
# Company name, address, total no of employees, Name of Director
# methods to set these attributes to print the data """

# class Company():
#     def __init__(self,name='xanthron',address='karaparamba',total_no_employee=11,director_name='hadhi'):
#         self.name = name
#         self.address = address
#         self.total_no_employee = total_no_employee
#         self.director_name = director_name
    
#     def display(self):
#         print('name of company: '+self.name,'company address: '+self.address,'no of emploee: '+str(self.total_no_employee),'director: '+self.director_name)

# c1 = Company()
# c1.display()
# # name of company: xanthron company address: karaparamba no of emploee: 11 director: hadhi

# """8. Write a python program to create a class named Triangle with method to calculate
# it’s area. """


#     # s = (a + b + c) / 2
#     # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# class Triangle():
#     def __init__(self, a, b, c):
#         self.first_side = a
#         self.secound_side  = b
#         self.third_side = c
    
#     def semi_perimiter(self):
#         self.s = (self.first_side + self.secound_side + self.third_side) / 2 

#     def area(self):
#         return (self.s * (self.s - self.first_side) * (self.s - self.secound_side) * (self.s - self.third_side)) ** 0.5

# newTriangle = Triangle(12, 10, 11)
# newTriangle.semi_perimiter()
# print(newTriangle.area())
# # 51.521233486786784

""" 9. Write a python program to print all unique subsets of two numbers from a given set
of distinct integer numbers using Oops techniques """

# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))
    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]

# print(py_solution().sub_sets([4,5,6]))
# # [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

