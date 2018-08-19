# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 01:02:42 2018
@author: Asmaa
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

""" Load your Datset """
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
""" : in the first means all cols and the second means the cols we need only """

""" Solving the problem of the missing values in the dataset """
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ='NaN' , strategy = 'mean', axis= 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

