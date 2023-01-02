# filter como el nombre lo dice filtra, >> filter(condicion_como_funcion, iterador)


people = [
    {'name':'Pedro', 'age': 30},
    {'name':'Juan', 'age': 50},
    {'name':'Pepe', 'age': 20},
    {'name':'Laura', 'age': 16},
    {'name':'Carolina', 'age': 18},
    {'name':'Felipe', 'age': 22},
]

# filtrar las personas mayores de 18

people_18 = list(filter( lambda x: x['age'] > 18 and x['name'].startswith('P') ,people))
#print(people_18)


countries = ["", "Argentina", "Colombia", None, "", "Bolivia", None]

countries_filtered = list(filter( lambda x: x != "" and x is not None , countries))
print(countries_filtered)