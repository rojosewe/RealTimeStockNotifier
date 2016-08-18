'''
Created on Aug 9, 2016

@author: root
'''

from rules import RuleLoader
import config.ConfigLoader as configurer
import config.Logger as logging
from tasks import RealTimeTasks, SleepUntilTomorrow
import reporters.PushBulletManager as pbm
import time

log = logging.getLogger()
log.info("Initializing RTSN")

symbols = []
# Map of stocks by symbol
stocks = {}
# Map of rules by symbol
rules = {}

rules = RuleLoader.load()
config = configurer.load()

for symbol in rules:
    symbols.append(symbol)

log.debug("loaded Rules for " + str(symbols))
tasks = []

pb = pbm.create(config["push-bullet-api-key"])

while True:
    time.sleep(SleepUntilTomorrow.getTimeSecondsUntilNextOpening())
    for symbol in symbols:
        task = RealTimeTasks.Task(symbol, symbol, config["refresh-time"], rules[symbol], pb)
        tasks.append(task)
        task.start()
        
    for task in tasks:
        task.join()
    
    log.info("RTSN ending. See you tomorrow")
    log.info("Sleeping until " + str(SleepUntilTomorrow.getNextOpeningTime()))
    