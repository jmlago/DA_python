#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:41:53 2017

@author: root
"""

import os
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
os.chdir("/home/josem/Escritorio/DA_python-master/scripts/dijous")

a = pd.read_csv("train.csv")
b = a[["Sex","Pclass","Age","SibSp","Parch","Survived"]].dropna()

ages = ["child","adult","old"]

b[ages[0]] = b["Age"].apply(lambda x: 1 if 0<x<15 else 0.) 
b[ages[1]] = b["Age"].apply(lambda x: 1 if 16<x<50 else 0.)
b[ages[2]] = b["Age"].apply(lambda x: 1 if 51<x<200 else 0.)
b["male"] = b["Sex"].apply(lambda x: 1 if x=="male" else 0.)
b["female"] = b["Sex"].apply(lambda x: 0 if x=="male" else 1.)
b["1r"] = b["Pclass"].apply(lambda x: 1 if x==1 else 0.)
b["2n"] = b["Pclass"].apply(lambda x: 1 if x==2 else 0.)
b["3d"] = b["Pclass"].apply(lambda x: 1 if x==3 else 0.)
b["No survived"] = b["Survived"].apply(lambda x: 1 if x==0 else 0.)

X = np.asarray([b[ages[0]],b[ages[1]],b[ages[2]],b["female"],b["male"],b["1r"],b["2n"],b["3d"]]).T
y = np.asarray([b["Survived"],b["No survived"]]).T
clf = MLPClassifier(activation="relu",solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7), random_state=1,verbose=True,max_iter=2000,validation_fraction=0.5)
a = clf.fit(X,y)
clf.score(X, y, sample_weight=None)


