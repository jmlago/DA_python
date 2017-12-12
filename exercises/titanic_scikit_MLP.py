#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:16:24 2017

@author: josem
"""

##Build the model with mxnet
import pandas as pd
import numpy as np
import os

dataset_path = "~/DA_python/datasets"

train_df = pd.read_csv(os.path.join(dataset_path,"processed_train.csv"), index_col=0)
test_df = pd.read_csv(os.path.join(dataset_path,"processed_test.csv"), index_col=0)

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

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(32,10,10,10), random_state=1,validation_fraction=0)

clf.fit(res_train_X, res_train_Y)

predictions_val = clf.predict(val_X)

def compute_accuracy(label,predicted):
    return np.sum(np.equal(label,predicted))/len(label)

acc = compute_accuracy(val_Y,predictions_val)


## Translate dataframes as np.matrices
train_X = train_df.as_matrix()[:,1:]## remove label column "Survived"
train_Y = train_df.as_matrix()[:,0]
test_X = test_df.as_matrix()

clf.fit(train_X, train_Y)

predictions_test = clf.predict(test_X)
