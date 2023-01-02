import logging

LOGGING_FORMAT = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_FILENAME = 'myapp.log'
logger = logging.getLogger('operation_file')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOGGING_FORMAT, LOGGING_DATE_FORMAT)
file_handler = logging.FileHandler(LOGGING_FILENAME)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





def division(num1, num2):

    logger.debug('accediendo al modulo aux')
    logger.debug(f"dividiendo por {num1} / {num2}")
    return num1 / num2