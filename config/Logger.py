import logging.config

logging.config.fileConfig('config/logging.conf')

logger = logging.getLogger('default')
# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

def getLogger():
    return logger
