# polimorfismo
# es hacer un overwriting de los metodos en las clases implementadas


class Auto:
    def desplazamiento(self):
        print('desplazamiento del auto')

class Moto:
    def desplazamiento(self):
        print('desplazamiento de la moto')

class Camion:
    def desplazamiento(self):
        print('desplazamiento del camion')

def corriendo_vehiculo(vehiculo):
    vehiculo.desplazamiento()

vehiculo = Auto()
corriendo_vehiculo(vehiculo=vehiculo)

vehiculo = Moto()
corriendo_vehiculo(vehiculo=vehiculo)

vehiculo = Camion()
corriendo_vehiculo(vehiculo=vehiculo)