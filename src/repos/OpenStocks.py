'''
Created on Aug 5, 2016

@author: rojosewe
'''

from yahoo_finance import Share
import datetime
from models.financial import HistoricalStock, CurrentStock

@staticmethod
def downloadHistorical(symbol, start='1970-01-01', end=None):
    if end is None:
        today = datetime.date.today()
        end = str(today[0])
    share = Share(symbol.upper())
    values = share.get_historical(start, end)
    stock = HistoricalStock(symbol)
    stock.info = share.get_info()
    stock.values = values 
    return stock

def downloadCurrent(symbol):
    share = Share(symbol.upper())
    stock = CurrentStock(symbol, share)
    return stock