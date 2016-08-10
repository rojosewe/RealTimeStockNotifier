import logging.config

# logging.config.fileConfig('config/logging.conf')

logging.basicConfig(filename='/var/log/RealTimeStockReview.log', format='%(asctime)s - %(module)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger('default')
# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

def getLogger():
    return logger
