import logging

def createLoggerForDev(self):
    logger = logging.getLogger('example')
    logger.setLevel(logging.ERROR)
