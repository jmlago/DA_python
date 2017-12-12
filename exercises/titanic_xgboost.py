#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:01:09 2017

@author: josem
"""

import pandas as pd
import numpy as np
import xgboost as xgb

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

## Instantiate the xgboost classifier
gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(res_train_X, res_train_Y)

## Predict labels in validation set
predictions_val = gbm.predict(val_X)

def compute_accuracy(label,predicted):
    return np.sum(label == predicted)/len(label)

acc = compute_accuracy(val_Y,predictions_val)


## Now we can train with full capacity
train_X = train_df.as_matrix()[:,1:]
train_Y = train_df.as_matrix()[:,0]
test_X = test_df.as_matrix()

gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(train_X, train_Y)
predictions_test = gbm.predict(test_X)
