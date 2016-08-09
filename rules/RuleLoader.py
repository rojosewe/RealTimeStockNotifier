import json

import config.Logger as logging

from rules import ThresholdGroup

log = logging.getLogger()

def load(root="rules-config/rules.json"):
    rules = {}
    __loadRules(root, rules)
    return rules

def __loadRules(root, rules):
    with open(root, "r+") as f:
        specs = json.load(f)
        __processRules(specs, rules)
        
def __processRules(specs, rules):
    for spec in specs:
        log.debug("Loading threshold rules" + json.dumps(spec))
        if "type" not in spec:
            log.error("Error loading rules. No type found.")
        if spec["type"].lower() == "external":
            __loadRules(spec["file"], rules)
        if spec["type"].lower() == "threshold":
            symbol = spec["symbol"]
            tg = ThresholdGroup.ThresholdGroup(symbol)
            result = tg.load(spec)
            __addRules(rules, symbol, result)

def __addRules(rules, symbol, newRules):
    if symbol not in rules:
        rules[symbol] = []
    symbol.append(newRules)