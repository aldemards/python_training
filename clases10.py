#clases abstractas, se utilizan como interface, bluprint.
# obligar a otros desarroladores que esan en nuestro equipo o 
# cuando colaboramos con codigo, a que sigan las implementaciones que se definen


from abc import ABC, abstractclassmethod

class Departamento(ABC):
    @abstractclassmethod
    def __init__(self, empleados):
        pass

    @abstractclassmethod
    def print_departamento():
        pass


class Contabilidad(Departamento):
    def __init__(self, empleados):
        self.empleados = empleados

    def print_departamento(self):
        print(f"Departamento de Contabilidad: {self.empleados}")

class Recursos_humanos(Departamento):
    def __init__(self, empleados):
        self.empleados = empleados

    def print_departamento(self):
        print(f"Departamento de Recursos: {self.empleados}")

class Administrativo(Departamento):
    def __init__(self, empleados):
        self.empleados = empleados
        self.empleados_base = empleados
        self.sub_dept = []

    def add(self, dept: Departamento):
        self.sub_dept.append(dept)
        self.empleados += dept.empleados

    def print_departamento(self):
        print('Departamento Administrativo')
        print(f"Departamento de admon Empleados base: {self.empleados_base}")
        for dept in self.sub_dept:
            dept.print_departamento()
        print(f"total de empleados: {self.empleados}")

cont = Contabilidad(25)
rh = Recursos_humanos(15)

main_dept = Administrativo(30)
main_dept.add(cont)
main_dept.add(rh)
main_dept.print_departamento()
