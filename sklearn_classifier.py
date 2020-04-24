# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:46:21 2019

@author: Andile XeroxZen
"""

#import numpy as np
from sklearn import tree

X = [[181, 80, 44], [177, 70, 43], [184, 84, 45], [183, 69, 40],[184, 76, 45], [183, 69, 39] ],[180, 70, 40], [177, 70, 43]

Y = ['male', 'female', 'male', 'female', 'female','male', 'male', 'female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)