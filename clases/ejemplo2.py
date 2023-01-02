# constructor

class Persona:
    
    def __init__(self, nombre_completo):
        self.nombre_completo = nombre_completo
        
    def saludar(self):
        print(f'hola {self.nombre_completo}')

    def get_name(self):
        print(f"nombre: {self.nombre_completo.split(' ')[0]}")

    def get_last_name(self):
            print(f"apellido: {self.nombre_completo.split(' ')[1]}")

andres = Persona('Andres Perez')

andres.saludar()
andres.get_name()
andres.get_last_name()



