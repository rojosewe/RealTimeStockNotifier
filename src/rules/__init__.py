'''
Created on Aug 9, 2016

@author: root
'''

import sys

class RuleType():
    
    def check(self, stock):
        raise Exception("Unimplemented abstract method")
    
    def translateToHuman(self):
        raise Exception("Unimplemented abstract method")