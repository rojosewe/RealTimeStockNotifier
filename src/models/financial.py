'''
Created on Aug 5, 2016

@author: rojosewe
'''

class HistoricalStock(object):
    '''
    Class for a stock`
    '''

    def __init__(self, symbol):
        '''
        Constructor
        '''
        self.symbol = symbol
        self.info = None
        self.values = []
        
class CurrentStock(object):
    '''
    Class for a stock`
    '''

    def __init__(self, symbol, share):
        '''
        Constructor
        '''
        self.symbol = symbol
        self.link = share
        self.map = {}
        self.refresh()
        
    def refresh(self):
        self.link.refresh()
        self.map["open"] = self.link.get_open()
        self.map["price"] = self.link.get_price()
        self.map["datetime"] = self.link.get_trade_datetime()
        self.map["prevClose"] = self.link.get_prev_close()
        self.map["change"] = self.link.get_change()
        self.map["daysLow"] = self.link.get_days_low()
        self.map["daysHigh"] = self.link.get_days_high()
        self.map["volume"] = self.link.get_volume()
        
    