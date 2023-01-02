# dependency inversion
from abc import ABC, abstractclassmethod

class Switcheable(ABC):
    @abstractclassmethod
    def prender(self):
        pass
    @abstractclassmethod
    def apagar(self):
        pass


class Bombillo(Switcheable):
    def prender(self):
        print('Bombillo: encendido')
    
    def apagar(self):
        print('Bombillo: apagado')

class Ventilador(Switcheable):
    def prender(self):
        print('Ventilador: encendido')
    def apagar(self):
        print('Ventilador: apagado')


# type hint
class EnergiaElectrica:
    def __init__(self, dispositivo:Switcheable):
        self.dispositivo = dispositivo
        self.encendido = False
    
    def presionar_interruptor(self):
        if self.encendido: # esto es igual a :  if self.encendido == True
            self.dispositivo.apagar()
            self.encendido = False
        else:
            self.dispositivo.prender()
            self.encendido = True
    
b = Bombillo()
v = Ventilador()

switch = EnergiaElectrica(b)
switch.presionar_interruptor()
switch.presionar_interruptor()
switch.presionar_interruptor()
switch_ventilador = EnergiaElectrica(v)
switch_ventilador.presionar_interruptor()
switch_ventilador.presionar_interruptor()