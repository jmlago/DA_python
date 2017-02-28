# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:16:51 2017

@author: JoseMaria

This is the practica2.py

The objective is to learn de basics of pandas.

Data from:
    https://www.kaggle.com/aljarah/xAPI-Edu-Data
"""
import os
import pandas as pd

##First of all tune the paths to your particular case
path = "C:\\Users\\JoseMaria\\Desktop\\codes"
os.chdir(path)
filename = "Edu-data.csv"
a = pd.read_csv(filename)

##First we want to know if Maths is a class of discussion or not
##That's important

b = a[["Topic","Discussion"]]

## Average name of discussions by topic
b.groupby("Topic").mean()

## if you have more discussions in history than in maths this is very bad

##Now lets see the grades by gender
marks = ["L","M","H"]

c = a[["gender","Topic","Class"]]

## I prefer to measure the grades by a number 0,1,2
import numpy as np
np.random.seed(1)
c["Class"].replace("L",3.5,inplace=True)
c["Class"].replace("M",8,inplace=True)
c["Class"].replace("H",9.5,inplace=True)

c.groupby("gender").mean()
c.groupby("Topic").mean()
c.groupby(["Topic","gender"]).mean()

c.groupby("Topic").mean().plot(kind="bar")

## Can we relate the parent school satisfaction with the grade?
a["Nota"] = c["Class"]

len(a[(a["ParentschoolSatisfaction"]=="Good") & a["Class"].isin(["H","M"])])
len(a[(a["ParentschoolSatisfaction"]=="Good") & a["Class"].isin(["L"])])
a[(a["ParentschoolSatisfaction"]=="Good") & a["Class"].isin(["L"])].describe()

c.to_csv("proba.csv",sep=";")
## so basically if the grades are good then the parent saring is good but with some exceptions
## this practice its about pandas not about statistics 
