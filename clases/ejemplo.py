

class User:
    def __init__(self, name, age):
        #constructor
        self.name = name
        self.age = age

    def get_age(self):
        return f"tengo {self.age} años"


persona1 = User('Antonio', 60)
persona2 = User('Sandra', 24)

print(persona1.get_age())
print(persona2.get_age())