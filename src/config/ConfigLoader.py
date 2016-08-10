import json

import config.Logger as logging

log = logging.getLogger()

def load(configFile="config/properties.json"):
    log.info("Loading the config from " + configFile)
    with open(configFile, "r+") as f:
        conf = json.load(f)
    validate(conf)
    return conf

def validate(conf):
    if "refresh-time" not in conf:
        log.warning("No Refresh rate set. Falling back to 20 miniutes")
        conf["refresh-time"] = 1200
        
