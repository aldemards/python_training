# la funcionalidad map se usa para optimizar el proceso de una función.

import math

PI = math.pi

def area_circulo(r):
    return PI * (r **2)

lista_radios = [5, 4, 8, 6, 9, 7, 23, 5]

areas = []
for r in lista_radios:
    a = area_circulo(r)
    areas.append(a)

#print(areas)
#print('___________________________________')
# el metodo map sirve para aplicar una funcion a un interable, retornar un objeto map
areas2 = list(map(area_circulo, lista_radios))

#print(areas2)


#ejercicio: hay una lista de temperaturas en grados celcius
# convertir estas temp a grados fahrenheit
# utilizar map y lambda

temp_c = [39.2, 36.5, 37.3, 37.8, 38.1 ,38.9]

#(0 °C × 9/5) + 32 

#def celsius_fahrenheit(tem):
#    return tem * (9/5) +32

temp_f = list(map(lambda tem: tem * (9/5) + 32 , temp_c))

#print(f'temperaturas °F: {temp_f}')

temp_c = [
    {'city': 'New York', 'temp_c': 39.2},
    {'city': 'London', 'temp_c': 36.2},
    {'city': 'Beijing', 'temp_c': 37.2},
    {'city': 'Tokio', 'temp_c': 37.8},
]

temp_f = list(map(lambda tem: tem['temp_c'] * (9/5) + 32 , temp_c))

print(temp_f)