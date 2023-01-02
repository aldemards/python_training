

class Dog():
    name = 'puppy'
    color = 'brown'
    def atributos(self): # funcion de instancia, por que contiene el parametro self
        return self.name, self.color



print(Dog.name)
perro1 = Dog()
perro1.name = 'firulais'
perro2 = Dog()
perro2.name = 'killer'
print(perro1.name)
print(perro2.name)
print(perro2.atributos())