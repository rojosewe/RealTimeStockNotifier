'''
Created on Aug 9, 2016

@author: root
'''
from rules import RuleLoader

symbols = []
rules = RuleLoader.load()

for symbol in rules:
    symbols.append(symbol)


        