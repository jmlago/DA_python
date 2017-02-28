# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:39:46 2017

@author: JoseMaria
Practica3 regex
"""

import re

##simple example
print(re.split(r'\s*',"This is what we want to split")) ##splits by spaces * means one or more

##This is quite easy but...

print(re.split(r'(\s*)',"This is what we want to split")) ## including spaces in the list

print(re.split(r'(s*)',"This is what we want to split")) ## splitting by s

print(re.split(r'[a-f]',"fñpaoehgañooahnañ-hwfvñougha`´ÓFHUAW`´OUGH")) ##splits by chars from a to f

##Python re are CASE SENSITIVE

print(re.split(r'[a-f][a-f]',"fñpaaaoehgañooahnañ-hwfvñoughaÓFHUAAWOUGH"))## splits by 2 combinations

print(re.split(r'[a-f][a-f]',"fñpaaaocehgañooahnañ-hwfvñoughaÓFHUAAWOUGH"))## splits by 2 combinations

print(re.findall(r'\d+',"dia 23 de cada mes")) ## one or more

print(re.findall(r'\d*',"dia 23 de cada mes del año 2017"))## zero or more

print(re.findall(r'\d{1,10}',"dia 23 de cada mes del año 201712351356245362546345633124513"))## zero or more

## so if we want to recognize a street

print(re.findall(r"calle\s+\w+\s+\d{1,5}","E la calle falsa 123 , vive Homer"))

print(re.findall(r"calle+[\w\s]+\d{1,5}","E la calle falsa o no tan falsa 123 , vive Homer"))##little bit more complex, but you can detect streets


import urllib.request

sites = "google yahoo instagram".split()

for s in sites:
    print("Searching "+s)
    u = urllib.request.urlopen("http://"+s+".com")
    text = u.read()
    title = re.findall(r"<title>+.*</title>+",str(text),re.I|re.M)
    print(title[0])
        
## more efficient compiled version of the pattern maybe you don't see now but
pattern = re.compile(r"<title>+.*</title>+")

for s in sites:
    print("Searching "+s)
    u = urllib.request.urlopen("http://"+s+".com")
    text = u.read()
    title = re.findall(pattern,str(text))
    print(title[0])

##trying to capture the speed
import time
start = time.time()
for i in range(10):    
    print("Searching google for iteration"+str(i))
    u = urllib.request.urlopen("http://google.com")
    text = u.read()
    title = re.findall(pattern,str(text))
    print(title[0])
end = time.time()
print("Elapsed time is "+str(end-start))

start = time.time()    
for i in range(10):    
    print("Searching google for iteration"+str(i))
    u = urllib.request.urlopen("http://google.com")
    text = u.read()
    title = re.findall(r"<title>+.*</title>+",str(text))
    print(title[0])
end = time.time()
print("Elapsed time is "+str(end-start))

##Regex that captures numbers in a string :) finally fixed
pattern = "[-+]?\d+[\.]?\d*[eE]?[-+]?\d*"
re.compile(pattern)
string = "Here I want to capture this 3 numbers, 1, -2.4"

re.findall(pattern,string)