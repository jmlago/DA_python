#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:35:25 2017

@author: josem
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from graphviz import Source

## Load preprocessed data
train_df = pd.read_csv('~/DA_python/datasets/processed_train.csv', header=0,index_col=0)
test_df = pd.read_csv('~/DA_python/datasets/processed_test.csv', header=0,index_col=0)


## Parameters to build validation set
proportion = .7
train_regs = int(proportion*len(train_df))

## New dataframes
val_df = train_df[train_regs:]
restricted_train_df = train_df[:train_regs]

## Translate dataframes as np.matrices
res_train_X = restricted_train_df.as_matrix()[:,1:]## remove label column "Survived"
res_train_Y = restricted_train_df.as_matrix()[:,0]
val_X = val_df.as_matrix()[:,1:]
val_Y = val_df.as_matrix()[:,0]

t = DecisionTreeClassifier()##max_depth=4

t.fit(res_train_X,res_train_Y)

## whichone is the best tree???
print("The score on train is "+str(t.score(res_train_X,res_train_Y)))
print("The score on validation is "+str(t.score(val_X,val_Y)))

export_graphviz(t,out_file="t.dot",class_names=["Survived","No survived"],feature_names=list(test_df.columns),impurity=False,filled=True)

with open("t.dot") as f:
    dot_graph = f.read()


s = Source(dot_graph, filename="test.gv", format="png")
## lets look at the tree
s.view()

## linux users sudo apt-get install graphviz
## mac users brew install graphviz
