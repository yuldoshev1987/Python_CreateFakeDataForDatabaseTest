import random as rdm
import math
#Write a Program to generate Fale Employee Data for database testing
#Employee Name
#Employee Number
#Employee Salary
#Employee City
#Employee Mobile Number
#Designation

#The name should contains 3 to 10 Characters
#First character should be upper case and remaining characters should be lower case
# Employee number should start 'e' followed by 4 digits
#example: e-1234
#Employee salary should be float value from 100000 50000
#Employee city should be from ['Waltham','Boston','Watertown','Natick','Framingham']
#Mobile number should contains exactly 10-digits where first number should be 5 to 7.
#example 5087985412
#Employee Designation should be from ['Software Engineer','Senior Software Engineer','Team Lead',
# 'Project Lead','Project Manager']


# Step-1 he name should contains 3 to 10 Characters,First character should be upper case
# and remaining characters should be lower case

def get_fake_name():
    name=''
    for i in  range(rdm.randint(3,10)):
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        name=name+str(rdm.choice(alphabet))
    return  name.capitalize()

#Step-2 Employee number should start 'e' followed by 4 digits Example: e-3201
def get_fake_enumber():
    enum='e-'
    for i in range(4):
        enum=enum+str(rdm.randint(0,5))

    return enum

#Step-3 Employee salary should be float value from 100000 50000
def get_fake_esalary():
    salary=round(rdm.uniform(10000,50000),2)
    return salary

#Step-4 Employee city should be from ['Waltham','Boston','Watertown','Natick','Framingham']
def get_fake_ecity():
    city=['Waltham','Boston','Watertown','Natick','Framingham','Acton','Billerica','Harvard','Middleborough']
    return rdm.choice(city)
#Step-5 Mobile number should contains exactly 10-digits where first number should be 5 to 7.

def get_fake_ephoneNumber():
    mobilenum=rdm.choice('5,6,7')
    for i in range(10):
        mobilenum=mobilenum+str(rdm.randint(0,9))
    return mobilenum
#Step-6 Employee Designation should be from

def get_fake_eDesignation():
    designation=['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']
    return rdm.choice(designation)
print(get_fake_eDesignation())

for i in range (50):
    enum=get_fake_enumber()
    eName=get_fake_name()
    designation=get_fake_eDesignation()
    salary=get_fake_esalary()
    city=get_fake_ecity()
    phoneNumber=get_fake_ephoneNumber()

    print('EmpEmployee Number:',enum,'Name:',eName,'Designation:',designation,'Salary:',salary,
          'City:',city,'Mobile Number',phoneNumber)