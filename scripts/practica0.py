#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 00:38:06 2016

@author: josem
"""

##PRACTICA 0

##Dynamic Typed

a = [1,2,3]
a = "pepito"
a = 2.54675

################### basic operators ###################

a = 2
b = 3

##for decimal numbers
a+b
a-b
a*b
a**b
b%a
b/a
a//b

##bitwise operators and all ints are binary in python3

a&b##AND binary copies common ones

a|b##OR binary copies all ones

a^b##XOR binary copies different ones

~a##flips all bits

##comparsion operators

a==b
a<b
a<=b
a>b
a>=b
a!=b

##membership operators
c = [a,b]
a in c
b not in c

del a,b,c ##free memory
#######################################################

################### numbers ###################

var1,var2,var3,var4 = int("1"),2,3.0,45

from math import *##not good way to import

##some strange function
def strange(x,y,z):
    return max(x,exp(floor(y)),fabs(z+x+y),)

var4 = strange(var1,var2,var3)

del var1,var2,var3,var4 ##free memory

###############################################

################### Strings ###################

a = "We are learning Python, and this are our first steps!!!"

a = 'We are learning Python, and this are our first steps!!!'

##This is not the same
a = """We are learning Python, and this are our first steps!!!"""

a = """We are learning 
    Python"""##because of this

b = " and this are our first steps!!!"

c = a+b ##overload operator +

##Accessing into the string REMIND THIS

c[:-3]
c[-3:]
c[:3]
c[3:]

##Attributes of the string object

c.count("e")##counts the number of substrings

c.find("are")##finds the position of the substrings

c.isalnum()##looks if all chars of the string are numerics

c.isdecimal()##looks if all chars of the string are decimal

c.lower()##change all capital letters for lower ones

c.replace("Python","Python basics")##replace substrings

##Converts the string into a list separated by target substring
c.split("are")

###############################################

################### Lists ###################

a = [1,2,3,"pepito",2.54675]

##Access into positions
a[0]
a[1]
print(a[3])

##Other useful attributes of lists

a.append(5)##add element into the list

a.pop(3)##delete the position not the number

a.remove(2.54675)##deletes the value

a = [2,65,1,435,12,2,76]

a.sort()

a.clear()##deletes all

a = [1,2,3,"pepito"]

b = [2,3,4,5]

c = a+b##overload operator +

del a,b,c
#############################################

################### Loops ###################

##for loops
for i in range(20):
    print("The main loop is "+str(i))

##nested loops
for i in range(20):
    for j in range(2):
        print("The nested loop of the main loop "+str(i)+" is "+str(j))

##while loops
a = 0

##take care of the while conditions
while a < 20:
    print(a)
    a=a+1
    
##if loops
if a is 20:
    print(a)
    a = a-1

##repeat
if a is 20:
    print(a)
    a = a-1

del a,i,j ##free everything

#############################################

################### os lib and files ###################

import os
path = "/home/josem/PythonCourse/practiques/practica0"

os.chdir(path)##change current work directory

os.listdir(path)##list all files in the path

textlist = []##initialize a list

##reads all files in the cwd and puts all files in textlist
for file in os.listdir():
    if file[-4:] == ".txt":
        with open(file,"r") as f:
            a = f.readlines()
            f.close()
    print(a)
    textlist.append(a)

newf = "/home/josem/PythonCourse/practiques/practica0/newf.txt"

for i in range(5):
    with open(newf,"a") as f:
        f.write("We are appending something into the newf\n")
        f.close()

########################################################

##The best help is online but you can always try this:
help()##Then type the object you want to look

