# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:47:52 2017

@author: JoseMaria
"""

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def grad(x):
    return x*(1-x)

X = np.array([[0],
             [0.2],
             [0.4],
             [0.6],
             [0.8],
             [1]])
y = np.array([[0],[1],[0],[1],[0],[0.999999]])

np.random.seed(1)

syn0 = 2*np.random.random((1,7))-1
syn1 = 2*np.random.random((7,7))-1
syn2 = 2*np.random.random((7,1))-1
 
for j in range(100000):
    l0 = X
    l1 = sigmoid(np.dot(l0,syn0))
    l2 = sigmoid(np.dot(l1,syn1))
    l3 = sigmoid(np.dot(l2,syn2))
    
    l3err = y - l3
    
    if j%10000 == 0:
        print(np.mean(np.abs(l3err))*100)
        print(syn0)
        print(syn1)
        print(np.mean(np.abs(l2err))*100)
        print(grad(l2))
        print(grad(l1))
    
        
    l3_d = l3err*grad(l3)        
    l2err = np.dot(l3_d,np.transpose(syn2))
    l2_d = l2err*grad(l2)
    l1err = np.dot(l2_d,np.transpose(syn1))
    l1_d = l1err*grad(l1)
    syn2 += np.dot(np.transpose(l2),l3_d)
    syn1 += np.dot(np.transpose(l1),l2_d)
    syn0 += np.dot(np.transpose(l0),l1_d)
    
print("Output is: "+str(l2))

def f(x,syn0,syn1,syn2):
    l1 = sigmoid(np.dot(x,syn0))
    l2 = sigmoid(np.dot(l1,syn1))
    l3 = sigmoid(np.dot(l2,syn2))
    return l3

import matplotlib.pyplot as plt


x = np.linspace(0, 1, 500)
fig, ax = plt.subplots()
newvalues = []
for el in x:
    newvalues.append(float(f(el,syn0,syn1,syn2)))
line1, = ax.plot(x, newvalues, '--', linewidth=2,
                 label='Hand Crafted NN')

ax.legend(loc='lower right')
plt.show()
