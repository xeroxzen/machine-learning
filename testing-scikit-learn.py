# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:05:51 2019

@author: Andile XeroxZen
"""

from sklearn import datasets

wine = datasets.load_wine()

features = wine.data
labels = wine.target

print("Number of entries: ", len(features))

for featurename in wine.feature_names:
    print(featurename[:10], "    \t"),
print("Class")
for feature, label in zip(features, labels):
    for f in feature:
        print(f, "\t\t"),
    print(label)