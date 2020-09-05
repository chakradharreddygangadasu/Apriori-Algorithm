# Apriori Algorithm

# Market basket analysis

""" The aim is to find the items list which are bought together by some association between the items
so that the item arrangement in the store could help to impo=rove sales. This can be achieved by Apriori algorithm"""
#importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing market basket dataset 
dataset = pd.read_csv('Market_Basket_Optimisation.csv')
"""Here the dataset is a dataframe but, for apriori model the data should be in the form of list which contains
each transaction as one list inside the list"""


transactions = []
for i in range(0,7501):
    transactions.append(str([dataset.values[i,j] for j in range(0,20)]))
    
##training aprior on the dataset
from mlxtend.frequent_patterns import apriori, association_rules  
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 0.3, min_length = 2)

##visualising the result
result = list(rules)

## in R we cann sort the rules by different criterioon like, lift,support or confidence while in python apriori takes 
## care of sorting, which is the relevent of combination of all support, confidence and lift
 
