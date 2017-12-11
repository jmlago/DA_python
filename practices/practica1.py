#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:55:26 2016

@author: root
"""

##PRACTICA 1

##numpy
import numpy as np

##initializing array
a = np.array([2,3,4])
b = np.array([3,4,5])

##some easy operations
a+b
np.dot(a,b)
a*b
a/b
b%a
a.shape
np.sum(a)

##other ways to initialize matrices
a = np.zeros([4,4])
a = np.ones([4,4])
a = np.full([4,4],7)
a = np.random.random([4,4])

##access into a position
a[2,3]

a = np.array([[1,2,3],[2,3,4],[3,4,5]])

##comparation operators
a > 2
a <= 2
a != 2

##different datatypes
a = np.array([1, 2], dtype=np.int64)
a = np.array([1, 2], dtype=complex)

##N-dimensional array
b = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
b.shape


# Array properties
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2
print(a.nbytes) # >>>200

# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]

print(a)
print(b)

# Incomplete Indexing
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]

print(b) 
print(c) 

# Where
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]

print(b)
a[b]

print(c)
a[c]

del a,b,c##free memory

##lets use some trick to interpolate with a generalized model
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0,6.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0,-1.0])
res = 1000000
for i in range(20):
    z,residuals, rank, singular_values, rcond = np.polyfit(x, y, i,full=True)#3 is the degree
    if residuals < res:
        a = z
#of the fitting polynomial
print(a)
p = np.poly1d(a)
p(0.45)

##Importing matplotlib
import matplotlib.pyplot as plt

plt.plot(x,y)
npoints = np.linspace(0,6,1000)
plt.plot(npoints,p(npoints))
plt.show()

## Compute the x and y coordinates for points on
## sine and cosine curves

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)





# Make the first plot
plt.subplot(2,1,1)
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()

##Let's do some scatter plot
for color in ['red', 'green', 'blue']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    plt.scatter(x, y, c=color, s=scale, label=color,
                alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()


