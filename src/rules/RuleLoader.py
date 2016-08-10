import json

import config.Logger as logging

from rules import ThresholdGroup

log = logging.getLogger()

def load(root="rules-config/rules.json"):
    log.info("Loading the rules from " + root)
    rules = {}
    __loadRules(root, rules)
    log.info("Rules loaded")
    return rules

def __loadRules(root, rules):
    log.debug("Loading rules from " + root)
    with open(root, "r+") as f:
        specs = json.load(f)
        __processRules(specs, rules)
        
def __processRules(specs, rules):
    for spec in specs:
        log.debug("Loading rules" + json.dumps(spec))
        if "type" not in spec:
            log.error("Error loading rules. No type found.")
        elif spec["type"].lower() == "external":
            __loadRules(spec["file"], rules)
        elif spec["type"].lower() == "threshold-group":
            symbol = spec["symbol"]
            tg = ThresholdGroup.ThresholdGroup(symbol)
            tg.load(spec)
            __addRules(rules, symbol, tg)

def __addRules(rules, symbol, newRules):
    if symbol not in rules:
        rules[symbol] = []
    rules[symbol].append(newRules)