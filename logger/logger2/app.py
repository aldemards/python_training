# pip install PyYAML
from operation import divison
import yaml
import logging
import logging.config

with open('simple.yaml') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
    

logger.debug(f'hola mundo')
divison(10,55)
logger.debug(f'dividiendo {10},{55}')