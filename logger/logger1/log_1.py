import logging
from aux_operation import division

LOGGING_FORMAT = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_FILENAME = 'myapp.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOGGING_FORMAT, LOGGING_DATE_FORMAT)
file_handler = logging.FileHandler(LOGGING_FILENAME)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




logger.debug(f'diviendo {10} / {2}')
print(division(10,2))
logger.debug(f'diviendo {10} / {0}')
print(division(10,0))
logger.debug(f'resultado de dividir {10} / {0}')