'''
Created on Aug 9, 2016

@author: root
'''

import config.Logger as logging

log = logging.getLogger()

def extractValueFromStock(stock, value):
    if value == "currentPrice":
        return stock.currenValue
    else:
        log.error("The value " + value + " for symbol " + stock.symbol + " is not valid.")
        