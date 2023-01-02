

def operacion(a, b):
    print('esto es una operacion')
    resultado = division(a,b)


def division(a, b):
    return a / b

#print(operacion(10,0))

#try except

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f'hay error de division por cero')
    except TypeError:
        print('estas dividiendo con strings')
    except Exception:
        print('algo salio mal')



#print(operacion(10,0))

#print(Exception.__subclasses__())


import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

start_time = time.time()
archivo = ''
try:
    logger.info('intentando abrir un archivo')
    #time.sleep(3)
    archivo = open('archivo_no_existente.txt')
    #raise Exception
except Exception as e:
    logger.error('El archivo fallo')
    archivo.close()
    logger.info('El archivo cerro')
finally:
    logger.info('yo me ejecuto siempre')
    logger.info(f' el script se demoro:{time.time()- start_time}')

print(operacion(10,0))