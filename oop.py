class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class Car(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"

class Motorcycle(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} revs the engine and starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} applies the brakes and stops"

# Creating instances of Car and Motorcycle
my_car = Car("Toyota", "Camry", 2020)
my_motorcycle = Motorcycle("Honda", "CBR500R", 2019)

# Using the start and stop methods without needing to know the internal implementation
print(my_car.start())
print(my_motorcycle.start())
print(my_car.stop())
print(my_motorcycle.stop())
