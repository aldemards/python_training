
class Car:
    wheels = 4
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
    
    def info(self):
        return f"{self.maker} {self.model}"

    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

    @classmethod
    def wheels_count(cls):
        return cls.wheels

#objeto == instancia de la clase

camion = Car('Toyota', 'Corolla')
print(camion.info())
print(Car.km_to_miles(100))
print('ruedas de mi clase',Car.wheels_count())
print('ruedas de mi objeto',camion.wheels)
camion.wheels = 16
print('ruedas de mi objeto', camion.wheels)
print(camion.wheels_count())
