'''
Created on Aug 9, 2016

@author: root
'''

from pushbullet import Pushbullet

def create(apiKey):
    return Pushbullet(apiKey)

def push(pb, stock, message):
    pb.push_note(stock.symbol, message)