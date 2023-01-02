# encapsulamiento 

class Prueba:
    def __init__(self, name):
        self.variable = name
        self._accesible = name
        self.__privada = name


p = Prueba('Jon')

#print(p.variable)
#print(p._accesible)
#print(p.__privada)

class Prueba2:
    def __init__(self, name):
        self.__name = name

    # getter
    @property
    def name(self):
        return self.__name

    # setter
    @name.setter
    def name(self, nuevo_nombre):
        self.__name = nuevo_nombre


p = Prueba2('Alejandra')
print(p.name)
p.name = 'alejandra'
print(p.name)

class Auto:
    def __init__(self, modelo, mecanismo_de_aceleracion):
        self.__modelo = modelo
        self.__mecanismo = mecanismo_de_aceleracion
        self.__tanque_combustible = 100

    def encender_luces(self):
        print('encendidas las luces')

    def acelerar(self):
        self.__inyectar_combustible(10)
        print(f'Aumentando velocidad en {self.__modelo} con la caja {self.__mecanismo}')

    def __inyectar_combustible(self, cantidad):
        self.__tanque_combustible -= cantidad
        return self.__tanque_combustible 

taxi = Auto('Renault', 'mecanica')

taxi.acelerar()

