# dunder methods == metodos especiales de clases
# metodos preconstruidos 

class Pizza:
    def __init__(self, name, ingredientes):
        self.name = name
        self.ingredientes = ingredientes

p = Pizza('jamon y queso', ['queso', 'jamon'])

#print(p) # <__main__.Pizza object at 0x0000024C28F07D60>

class Pizza:
    ''' esta clase sirve para crear pizzas y tiene la funcionalidad de mostrar los ingredientes'''
    def __init__(self, name, ingredientes):
        self.name = name
        self.ingredientes = ingredientes
    def __str__(self):
        return  f"Descripcion del objeto: Pizza de {self.name}"
    def __repr__(self):
        return self.ingredientes 

    def __len__(self):
        return len(self.ingredientes)

    def __eq__(self, otra_clase):
        if self.ingredientes == otra_clase.ingredientes:
            return True
        else:
            return False 
    

p1 = Pizza('jamon y queso', ['queso', 'jamon'])
p2 = Pizza('jamon y queso', ['queso', 'jamon'])


#print(p1)
#print(p1.__doc__)
#print(p1 == p2)
#print(p1.__eq__(p2))
print(len(p1))



#print(dir(p))

#https://docs.python.org/3/reference/datamodel.html#special-method-names