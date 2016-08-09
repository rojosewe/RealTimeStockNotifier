'''
Created on Aug 9, 2016

@author: root
'''

import utils.StockUtils as u
import config.Logger as logging

log = logging.getLogger()

class Threshold(object):
    '''
    classdocs
    '''

    def __init__(self, symbol, operation, value):
        self.symbol = symbol
        self.operation = operation
        self.value = value
        
    def check(self, stock):
        currentValue = u.extractValueFromStock(stock, self.value) 
        if self.operation == "eq":
            return currentValue == self.value
        elif self.operation == "le":
            return currentValue <= self.value
        elif self.operation == "lt":
            return currentValue < self.value
        elif self.operation == "ge":
            return currentValue >= self.value
        elif self.operation == "gt":
            return currentValue > self.value
        else:
            log.error("The operation " + self.operation + " for symbol" + self.symbol + " is not valid")
            