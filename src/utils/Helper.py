'''
Created on Aug 5, 2016

@author: rojosewe
'''

def StockToSingleValueStream(stock, value="Close"):
    """
    Value it can be Adj_Close, Close, Date, High, Low, Open, Volume.
    """
    data = []
    for v in stock.values:
        data.append(v[value])
    return data
        
        