# static methods and class methods 

#class method

# Pizza([mozzarela, pimenton])

class Pizza:
    contador = 1
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    def __str__(self):
        return f"Pizza : {self.ingredientes}"

    @classmethod
    def margherita(cls):
        cls.contador += 1
        return cls(['mozzarela', 'tomates']), cls.contador

#p = Pizza.margherita()
p2 = Pizza(['jamon','queso'])
p3 = Pizza(['jamon','piña'])

""" print(p2.contador)
print(p3.contador)
print(p2.margherita())
print(p2.contador)
print(p3.contador)
print(p3.margherita())
print(p2.contador)
print(p3.contador)
 """
import math


class Pizza:
    contador = 1
    def __init__(self, radio, ingredientes):
        self.ingredientes = ingredientes
        self.radio = radio    
    def __str__(self):
        return (f"Pizza {self.radio},{self.ingredientes}")

    def area(self):
        return self.area_del_circulo(self.radio)
    
    @staticmethod
    def area_del_circulo(r):
        return r**2 *math.pi

p = Pizza(4, ['jamon','piña'])
print(p.area())

print(Pizza.area_del_circulo(582))
