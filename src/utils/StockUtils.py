'''
Created on Aug 9, 2016

@author: root
'''

import config.Logger as logging

log = logging.getLogger()

def extractValueFromStock(stock, value):
    if not value in stock.map:
        raise ValueError("The value " + value + " for symbol " + stock.symbol + " is not valid.")
    else:
        return float(stock.map[value])
        
        