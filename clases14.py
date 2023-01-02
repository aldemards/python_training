# typing hint
#meramente documental
x = 1 
x:str = 25

def add_numbers(a:int, b:int) -> None:
    print(a+b)

add_numbers(2,5)

def add_numbers(a:int, b:int, c:int) -> int:
    return a+b+c

# [[1,2,3],[5,8,5]]
from typing import List, Dict
from unicodedata import name

x:List[List[int]] = [[1,2,3],[5,8,5]]
print(x)

#{key:vale} ---- Dict[key, value]
x: Dict[str,int] = {"edad":25, "altura": 250}

Vector_complejo = List[float]

def print_vector(v:Vector_complejo):
    print(v)

from typing import Optional, Any, Callable

def foo(output:Optional[bool]=False):
    pass

def foo(output:Any):
    pass

def funcion_de_funcion(func:Callable[[int, int], None]) -> int:
    a = func(1,2)
    return a

from pydantic import BaseModel

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.verificar_parametros()

    def verificar_parametros(self):
        if type(self.name) == str:
            self.name = name
        else:
            raise ValueError

    def __str__(self):
        return f"{self.name}, {self.name}"

p = Persona('juan', 32)
print(p)


# class Persona(BaseModel):
#     name:str
#     age: str