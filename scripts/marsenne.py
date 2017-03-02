#!/usr/bin/python
# File: sum_primes.py
# Computes the sum of prime numbers under a integer in parallel
from math import sqrt
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def is_prime(n):
  r = int(sqrt(n))
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f += 6
  return True  

def lltest2(n,sed,acc,f,rank):
	t = True
	a = 2**n-1
	s = sed
	for i in range(acc,n):
		b = (s**2-2)
		if t and b > a and s != sed:
			sed = s
			acc = acc +1
			t = False
		s = b%a
		if t and (b > s):
			t = False		
	if s == 0: 
		f.write(str(n)+" provided by node "+str(rank)+"\n")
	return sed, acc

acc = 2
sed = 4
r = rank*6
with open("primers.txt","a") as f:
	for i in range(1,8,3):
		sed, acc = lltest2(i+rank,sed,acc,f,rank)
	for i in range(11,11500,6*size):
		a = i + r
		b = a + 2
		if is_prime(a): 
			sed, acc = lltest2(a,sed,acc,f,rank) 
		if is_prime(b): 
			sed, acc = lltest2(b,sed,acc,f,rank)
