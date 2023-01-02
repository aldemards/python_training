# Enum enumerador 


# utilizando el metodo enumerate en loop

lista_nombres = ['Juan', 'Pedro', 'Sandra','Carolina']
""" 
for nombre in lista_nombres:
    print(nombre)

for i, nombre in enumerate(lista_nombres):
    print(i, nombre)

for i in range(len(lista_nombres)):
    print(i, lista_nombres[i])
 """
# utilizando enumerate como clase 

from enum import Enum

class Fuel(Enum):
    DIESEL = 1
    GASOLINA = 2
    EXTRA = 3



class Car:
    def __init__(self, fuel):
        self.fuel = fuel

    def get_fuel(self):
        if self.fuel.value == 1:
            print('descuento por combustible diesel')
        return self.fuel

c = Car(Fuel.DIESEL)
#print(c.get_fuel())

#print(Fuel.EXTRA.value)

class Color(Enum):
    rojo = '#ff0000'
    verde = '#08000'
    azul = '#0000ff'

print(Color.verde.value)
print(Color('#08100'))