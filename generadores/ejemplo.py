
def genera_multiplos_de_7(limite):
    numero = 1
    lista=[]
    while numero < limite:
        if numero % 7 == 0:
            lista.append(numero)
        numero += 1
    return lista

print(genera_multiplos_de_7(50))

#for i in genera_multiplos_de_7(50):
#    print(i)

def genera_multiplos_de_7_generador(limite):
    numero = 1
    while numero < limite:
        if numero % 7 == 0:
            yield numero
        numero += 1

'primer valor'
generador = genera_multiplos_de_7_generador(50)
print(next(generador))

'segundo valor'
print(next(generador))