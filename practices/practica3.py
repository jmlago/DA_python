# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:39:46 2017

@author: JoseMaria
Regex
"""

import re

##simple example
print(re.split(r'\s*',"This is what we want to split")) ##splits by spaces * means one or more

##This is quite easy but...

print(re.split(r'(\s*)',"This is what we want to split")) ## including spaces in the list

print(re.split(r'(s*)',"This is what we want to split")) ## splitting by s

print(re.findall(r'\d+',"dia 23 de cada mes")) ## one or more

print(re.findall(r'\d*',"dia 23 de cada mes del año 2017"))## zero or more

print(re.findall(r'\d{1,10}',"dia 23 de cada mes del año 201712351356245362546345633124513"))## zero or more

## so if we want to recognize a street

print(re.findall(r"calle\s+\w+\s+\d{1,5}","En la calle falsa 123 , vive Homer"))

print(re.findall(r"calle+[\w\s]+\d{1,5}","En la calle falsa o no tan falsa 123 , vive Homer"))##little bit more complex, but you can detect streets

##Regex that captures numbers in a string finally fixed
pattern = "[-+]?\d+[\.]?\d*[eE]?[-+]?\d*"
re.compile(pattern)
string = "Here I want to capture this 3 numbers, 1, -2.4"

re.findall(pattern,string)