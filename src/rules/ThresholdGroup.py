'''
Created on Aug 9, 2016

@author: root
'''
from rules import RuleType
from rules.Threshold import Threshold

class ThresholdGroup(RuleType):
    '''
    classdocs
    '''

    def __init__(self, symbol):
        self.symbol = None
        self.group = []
        
    def load(self, json):
        self.symbol = json["symbol"]
        for cond in json["conditions"]:
            field = cond["field"]
            operation = cond["op"]
            value = cond["value"]
            t = Threshold(self.symbol, field, operation, value)
            self.group.append(t)
        return self.group
     
    def check(self, stock):
        for t in self.group:
            if not t.check(stock):
                return False
        return True
    
    def translateToHuman(self):
        msg = ["All these thresholds have been met: \n"]
        for t in self.group:
            msg.append(t.translateToHuman())
        return "\n".join(msg)