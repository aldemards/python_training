#herencia

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


class Hyundai(Auto):
    def __init__(self, mecanismo_de_aceleracion):
        super().__init__('Hyundai', mecanismo_de_aceleracion)

    def accionar_exploradoras(self):
        print('accionando exploradoras')
        

taxi = Hyundai('automatico')
taxi.acelerar()
taxi.encender_luces()
taxi.accionar_exploradoras()