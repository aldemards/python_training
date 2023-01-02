# herencia multiple, no todos pueden hacer esto (lenguajes de programcion)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Encargado:
    def __init__(self, codigo_encargado, departamento):
        self.codigo_encargado = codigo_encargado
        self.departamento = departamento

# como minimo se le debe pasar al constructor los argumentos de la primera clase
class Estudiante_Encargado(Persona, Encargado):
    def __init__(self, nombre, edad, clave, calificacion, codigo_encargado, departamento):
        Persona.__init__(self, nombre, edad)
        Encargado.__init__(self, codigo_encargado, departamento)
        self.clave = clave
        self.calificacion = calificacion
        self.codigo_encargado = codigo_encargado
        self.departamento = departamento

class Estudiante(Persona):
    def __init__(self, nombre, edad, clave, calificacion):
        super().__init__(nombre, edad)
        self.clave = clave
        self.calificacion = calificacion

estudiante_encargado_1 = Estudiante_Encargado("Juan",22, "fa4532", 10,"123", "sistemas")
print(estudiante_encargado_1.nombre, estudiante_encargado_1.departamento)