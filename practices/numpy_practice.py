#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:47:20 2017

@author: josem
"""

##Numpy exercise
import numpy as np
import time
## Arrays and scalars
a = np.array([1, 2, 3, 4])
a + 1

2**a

## All arithmetic operates elementwise
b = np.ones(4) + 1
a - b

a * b## this is not matrix product


j = np.arange(5)
2**(j + 1) - j

## Is numpy fast?
## using numpy
start = time.time()
for i in range(10000):
    a = np.arange(10000)
    b = a+1
print("%16G seconds"%(time.time()-start))

## using pure python
start = time.time()
for i in range(10000):
    a = range(10000)
    b =  [i+1 for i in a] 
print(str(time.time()-start)+" seconds")

## Around 30 times faster

## Warning, not matrix multiplication
c = np.ones((3, 3))
c * c

## Real matrix multiplication
c.dot(c)
np.dot(c,c)

## Comparison operators
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b

a > b

## Arraywise comparisons
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
np.array_equal(a, b)

np.array_equal(a, c)

## Applying vectorial functions
a = np.arange(5)
np.sin(a)
np.log(a)
np.exp(a)

## Transpose matrix
a = np.triu(np.ones((3, 3)), 1)   # upper triangular
a
a.T
np.transpose(a)

## Minmax functions
x = np.array([1, 3, 2])
x.min()
x.max()
x.argmin()  # index of minimum
x.argmax()  # index of maximum

## Statistics
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()
np.median(x)
np.median(y, axis=-1)## last axis
x.std()

## Reshaping
a.reshape(-1)

## Change specific entries
a[0,0] = 100

## Numpy where
a[np.where(a == 1)] = 2

