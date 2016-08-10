'''
Created on Aug 10, 2016

@author: rojosewe
'''

import datetime
import config.Logger as logging

log = logging.getLogger()



def getTimeSecondsUntilNextOpening():
    opening = getNextOpeningTime()
    td = opening - datetime.datetime.now()
    if td.days > 1:
        diff = td.days * 24 * 60 * 60 + td.seconds
    else:
        diff = td.seconds
    log.info("next opening time at " + str(opening))
    return diff

def getNextOpeningTime():
    weekday = datetime.datetime.today().weekday()
    hour = datetime.datetime.now().hour
    if weekday == 7:
        nextDay = datetime.date.today() + datetime.timedelta(days=1)
    elif weekday == 6:
        nextDay = datetime.date.today() + datetime.timedelta(days=2)
    else:
        if hour >= 0 and hour < 16:
            nextDay = datetime.date.today()
        elif hour >= 16 and hour < 22:
            return 0
        else:
            nextDay = datetime.date.today() + datetime.timedelta(days=1)
    opening = datetime.datetime.strptime(str(nextDay) + " 16:00:00", '%Y-%m-%d %H:%M:%S')
    return opening

def getNextClosingTime():
    weekday = datetime.datetime.today().weekday()
    hour = datetime.datetime.now().hour
    if weekday == 7:
        nextDay = datetime.date.today() + datetime.timedelta(days=1)
    elif weekday == 6:
        nextDay = datetime.date.today() + datetime.timedelta(days=2)
    else:
        if hour >= 0 and hour < 16:
            nextDay = datetime.date.today()
        elif hour >= 16 and hour < 22:
            nextDay = datetime.date.today()
        else:
            nextDay = datetime.date.today() + datetime.timedelta(days=1)
    closingTime = datetime.datetime.strptime(str(nextDay) + " 22:00:00", '%Y-%m-%d %H:%M:%S')
    log.info("next closing time at " + str(closingTime))
    return closingTime