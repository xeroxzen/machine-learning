# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:44:16 2019

@author: Andile XeroxZen
"""

import numpy as np
import seaborn as sns

data = np.random.randn(100)
sns.distplot(data, kde=True, rug=True)