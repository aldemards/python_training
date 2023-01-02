#Dependency inyection

class Pais:
    def __init__(self, nombre, presidente):
        self.nombre = nombre
        self.presidente = presidente

    def __str__(self) -> str:
        return f"Pais {self.nombre}, presidente {self.presidente}"

class Ciudad:
    def __init__(self, nombre, habitantes, pais):
        self.nombre = nombre
        self.habitantes = habitantes
        self.pais = pais

    def __str__(self) -> str:
        return f"Ciudad {self.nombre}, N° Hab {self.habitantes}, pais {self.pais}"

colombia = Pais('Colombia', 'Petro')
medellin = Ciudad('Medellin', '5M', colombia)

print(medellin)