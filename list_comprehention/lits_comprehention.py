# obtener el mismo resultado de iterar sobre listas pero de una manera más eficiente

# obtener el cuadrado de los primeros 10 numeros

squares = []

for i in range(1,11): # obetenemos con range(1,11) un rango iterable de 1 a 10
    squares.append(i**2)

#print(squares)

squares2 = [i**2 for i in range(1,11)]

#print(squares2)

list_movies = ["Star Wars", "Gandhi", "Casablanca", "The Godfather", 
"The Blues Brothers", "Ghostbusters","Kill Bill", "The Matrix","Groundhog Day","Goodfellas"]

gmovies = []
for movie in list_movies:
    movie.title()
    if movie[0] == 'G':
        gmovies.append(movie)

#print(gmovies)


# movie: es la variable que quiero obtener en mi lista (append) (cualquie nombre) 
# list_movies: la lista iterable (la lista de peliculas)          
#  variable for variable in lista_que_tengo if variable (condicional ==, !=, >) condicion
gmovies2 = [movie for movie in list_movies if movie.title()[0] == 'G']

#print(gmovies2)

movies = [
    {"title": "Star Wars", "year": 1977},
    {"title": "Gandhi", "year": 1982},
    {"title": "Casablanca", "year": 1942},
    {"title": "The Godfather", "year": 1972},
    {"title": "The Blues Brothers", "year": 1980},
    {"title": "Ghostbusters", "year": 1984},
    {"title": "Kill Bill", "year": 2003},
    {"title": "The Matrix", "year": 1999},
    {"title": "Groundhog Day", "year": 1993},
    {"title": "Goodfellas", "year": 1990}
]

peliculas_antes_de_2000 = [movie["title"]  for movie in movies if movie["year"] < 2000]
peliculas2_antes_de_2000 = [{"titulo_pelicula":title["title"], "año_pelicula":title['year']} for title in movies if title["year"] < 2000]

#print(peliculas_antes_de_2000)
print(peliculas2_antes_de_2000)


