from repos import OpenStocks as os
import time
import datetime
import threading
import config.Logger as logging
import reporters.PushBulletManager as pbm
from tasks import SleepUntilTomorrow

log = logging.getLogger()

class Task(threading.Thread):
    def __init__(self, threadID, symbol, refreshRate, rules, notifier):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.symbol = symbol
        self.refreshRate = refreshRate
        self.rules = rules
        self.notifier = notifier
        self.closingTime = SleepUntilTomorrow.getNextClosingTime()
    
    def run(self):
        log.info("Running task for " + self.symbol)
        stock = os.downloadCurrent(self.symbol)
        while datetime.datetime.now() < self.closingTime:
            try:
                for rule in self.rules:
                    if rule.check(stock):
                        msg = rule.translateToHuman()
                        log.info(msg)
                        pbm.push(self.notifier, self.symbol, msg)
                time.sleep(self.refreshRate)
                stock.refresh()
            except ValueError as e:
                log.error(e)
                break