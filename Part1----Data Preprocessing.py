# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:57:35 2018

@author: Asmaa
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
""" : in the first means all cols and the second means the cols we need only """

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ='NaN' , strategy = 'mean', axis= 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

