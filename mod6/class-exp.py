class Student:
    regno = 101
    name = 'Madhav'
    age = 15
    def display(self):
        print(self.name)

s1 = Student()
s1.display()
# Madhav

# change name
s1.name = 'shankar'
s1.display()
# shankar

# inheritence
class Person():
    def __init__(self,name='madhav',age=15,email='madhav@gmail.com',phone=12345678):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
    def show(self):
        print (self.name)

class Student(Person):
    def __init__(self,regno=123,batch='A'):
        self.regno = regno
        self.batch = batch
    def display(self):
            print(self.name,self.regno,self.batch)

stud1=Student()
stud1.name = 'shankar'
stud1.regno=5555
stud1.batch='B'
stud1.show()
# shankar
stud1.display()
# shankar 5555 B
