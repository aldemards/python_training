import logging


logger = logging.getLogger(__name__)

def divison(a, b):
    logger.debug('accediendo al modulo operation')
    logger.debug('Dividiendo %s / %s', a, b)
    return a / b