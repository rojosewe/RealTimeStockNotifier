'''
Created on Aug 9, 2016

@author: root
'''

import utils.StockUtils as u
import config.Logger as logging
from rules import RuleType

log = logging.getLogger()

class Threshold(RuleType):
    '''
    classdocs
    '''

    def __init__(self, symbol, field, operation, value):
        self.symbol = symbol
        self.field = field
        self.operation = operation
        self.value = value
        self.__loadRule()
        
    def __loadRule(self):
        if self.operation == "eq":
            self.action = self.__eq
        elif self.operation == "le":
            self.action = self.__le
        elif self.operation == "lt":
            self.action = self.__lt
        elif self.operation == "ge":
            self.action = self.__ge
        elif self.operation == "gt":
            self.action = self.__gt
        else:
            log.error("The operation " + self.operation + " for symbol" + self.symbol + " is not valid")
                
    def __eq(self, currentValue):
        return currentValue == self.value
        
    def __le(self, currentValue):
        return currentValue <= self.value
    
    def __lt(self, currentValue):
        return currentValue < self.value
    
    def __ge(self, currentValue):
        return currentValue >= self.value
    
    def __gt(self, currentValue):
        return currentValue > self.value
    
    def check(self, stock):
        currentValue = u.extractValueFromStock(stock, self.field)
        log.debug("Comparing  " + self.field + " current: " + str(currentValue) + " " + self.operation + " " + str(self.value))
        return self.action(currentValue) 
        
        
    def translateToHuman(self):
        translateDict = {}    
        translateDict["eq"] = "is equal to"
        translateDict["le"] = "is less than"
        translateDict["lt"] = "is less or equal than"
        translateDict["ge"] = "is greater or equal than"
        translateDict["gt"] = "is greater than"
        msg = "The stock " + self.symbol + "'s " + self.field + " " + translateDict[self.operation] + " " + str(self.value)
        return msg