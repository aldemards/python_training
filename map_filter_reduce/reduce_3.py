# reduce se utiliza para reducir una lista a un solo valor
# reduce(function, iterable)
# funciona como una funcion de acumulacion
# ej: se tiene una lista de numeros
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y una fucnion de acumulacion
# def accumulator(x, y):
#     return x + y
#
# # reduce la lista a un solo valor
# # reduce(accumulator, lista)

# en la primera iteracion x = 1 y y = 2 y la respuesta es resultado = 3
# en la segunda iteracion x = resultado  y y = 4
# en la tercera iteracion x = resultado  y y = 5
# en la cuarta iteracion x = resultado  y y = 6
# en la quinta iteracion x = resultado  y y = 7
# y asi sucesivamente

from functools import reduce 

values = [1,2,3,4]

resultado = 1
for value in values:
    resultado *= value
print(resultado)
##________________________________

def accumulator(x, y):
    return x * y

resultado = reduce(accumulator, values)
print(resultado)
