# w - write - escribe en el archivo si no existe lo crea y si existe lo sobreescribe
# r - read - lee el archivo
# a - append - agrega al final del archivo
# r+ - read and write - lee y escribe en el archivo
# w+ - write and read - escribe y lee en el archivo
# a+ - append and read - agrega al final y lee en el archivo
# rb - read binary - lee en binario
# wb - write binary - escribe en binario

""" # abro el archivo
f = open('texto2.txt','w')
# leo el archivo
print(f.write(" hola mundo"))
# cerrar el archivo
f.close() """

# para solucionar el problema de olvidar el close existe el context manager --> with
""" 
with open('texto.txt','r') as f:
    for line in f:
        print(line, end='')
    #print(f.readlines()) """

with open('texto.txt','r') as f:
    with open('archivo_copia.txt', 'w') as f_copy:
        f_copy.write(f.read())
