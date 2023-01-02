# @decorador
# def suma(a,b)
#     return a+b


# nombre_decorador( funcion a decorar) -> nueva funcion


def imprimir_antes(funcion):
    def nueva_funcion():
        print('entro a la funcion')
        funcion()
        print('salio de la funcion')
    return nueva_funcion


@imprimir_antes
def saludar():
    print('hola mundo')

@imprimir_antes
def saludar2():
    print('esto es otra funcion')



#saludar()
#saludar2()


def decorador_parametros(funcion):
    def nueva_funcion(*args,**kwargs):
        if len(args) < 2:
            raise TypeError('La funcion requiere 2 parametros')
        return funcion(*args,**kwargs)
    return nueva_funcion

@decorador_parametros
def suma(a,b):
    return a + b

print(suma(1,2))
print(suma(1))

