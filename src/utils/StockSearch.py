'''
Created on Aug 5, 2016

@author: rojosewe
'''

def byDate(stock, date):
    alist = stock.values
    first = 0
    last = len(alist)-1
    pos = -1 

    while first<=last:
        midpoint = (first + last)//2
        if alist[midpoint]["Date"] == date:
            pos = midpoint
            break
        elif date < alist[midpoint]["Date"]:
            last = midpoint-1
        else:
            first = midpoint+1
    return pos