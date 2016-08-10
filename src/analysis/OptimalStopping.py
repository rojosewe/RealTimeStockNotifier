'''
Created on Aug 5, 2016

Implementation of Optimal Stopping in the stock market when the future is discounted by Mark Finster

@author: rojosewe
'''

import numpy as np
from utils import Helper

def calculateOverHistoric(data, gamma=0.0056):
    '''
    Gamma is calculated where max time is 6 months. I don't care about infinity
    '''
    if len(data) == 0:
        return None 
    if "Close" in data.values[0]:
        Helper.StockToSingleValueStream(data)
    data = np.array(data)
    stdDev = np.std(data)
    mean = np.mean(data)
    aov = __approxOptimalValue(data, mean, gamma)
    
def __approxOptimalValue(data, mean, gamma):
    c = mean/(1 - gamma)