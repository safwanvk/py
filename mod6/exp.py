# Image manipulation in python

# PIL(Python Image Library), opencv, simplecv, Imagemagick

# PIL
from PIL import Image, ImageFilter
img = Image.open('dog.jpg')
img.rotate(45).show()
img_sharp = img.filter( ImageFilter.SHARPEN )
mg_grey = img.convert("L")
img_sharp.show()
img_grey.show()

# opencv
import cv2
img = cv2.imread('dog.jpg') # read
cv2.imshow('image',img) # show
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mysql
import MySQLdb
db = MySQLdb.connect(
host="127.0.0.1", # your host
user="root", # username
password="", # password
db="test") # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# # Create Table
cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# # Insert
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cur.execute(sql, val)

db.commit()

print(cur.rowcount, "record inserted.")


# Select data from table using SQL query.
cur.execute("SELECT * FROM customers")

# print the first and second columns
for row in cur.fetchall() :
    print(row[0], " ", row[1])
# John Highway 21

result = cur.fetchall()
for i in result:
    print(i)
#('john','Highway 21')

# Drop table if it already exist using execute() method.
cur.execute("DROP TABLE IF EXISTS customers")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT )"""
cur.execute(sql)

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # Execute the SQL command
    cur.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    db.close()

cur.execute("SELECT * FROM EMPLOYEE")
result = cur.fetchall()
for i in result:
    print(i)

# Postgresql

import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres",
password = "postgres", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

# Craete Table
cur.execute("""CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL)""")

print('Table created successfully')

# Add data to table
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1,'abu',12,'California',20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2,'aju',12,'Texas',15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3,'shankar',18,'Norway',20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4,'shake',21,'Rich-Mond ',65000.00 )")

conn.commit()
print('Records created successfully')

# Fetch data 
cur.execute("SELECT id, name, address, salary from COMPANY")
rows = cur.fetchall()
for row in rows:
    print('ID = ', row[0])
    print('NAME = ', row[1])
    print('ADDRESS = ', row[2])
    print('SALARY = ', row[3], '\n')

conn.commit()
conn.close()

"""ID =  1
NAME =  abu
ADDRESS =  California                                        
SALARY =  20000.0 

ID =  2
NAME =  aju
ADDRESS =  Texas                                             
SALARY =  15000.0 

ID =  3
NAME =  shankar
ADDRESS =  Norway                                            
SALARY =  20000.0 

ID =  4
NAME =  shake
ADDRESS =  Rich-Mond                                         
SALARY =  65000.0 """