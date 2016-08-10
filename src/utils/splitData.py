import utils

def fromDateOn(stock, date):
    pos = utils.StockSearch.byDate(stock, date)
    newStock = stock.clone()
    if pos < 0:
        if newStock.values[0]["Date"] > date:
            newStock.values = []
        return newStock
    newStock.values = newStock.values[pos:] 
    return newStock

def BeforeDate(stock, date):
    pos = utils.StockSearch.byDate(stock, date)
    newStock = stock.clone()
    if pos < 0:
        if newStock.values[0]["Date"] > date:
            newStock.values = []
        return newStock
    newStock.values = newStock.values[:pos] 
    return newStock