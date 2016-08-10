'''
Created on Aug 9, 2016

@author: root
'''
import config.Logger as logging
from pushbullet import Pushbullet

log = logging.getLogger()

def create(apiKey):
    return Pushbullet(apiKey)

def push(pb, symbol, message):
    log.info({"Sending notification: " + message})
    pb.push_note("RTSN announces!!", message)