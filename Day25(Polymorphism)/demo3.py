# Overriding methods
class Vehicle:

    def speed(self):
        print('Vehicle speed is 40kmph')


class Car(Vehicle):

    def speed(self):
        print('Car speed is 100kmph')
        super().speed()


class Truck(Vehicle):

    def speed(self):
        print('Truck speed is 80kmph')
        Car().speed()


obj_Truck = Truck()
obj_Truck.speed()

# Truck speed is 80kmph
# Car speed is 100kmph
# Vehicle speed is 40kmph

# A base class: Vehicle with a method speed().
# Two derived classes: Truck and Car, both overriding the speed() method.
# This is runtime polymorphism:
# The method speed() behaves differently depending on the object calling it (Truck, Car, or Vehicle).
# Method calls are resolved at runtime — that's why it’s called dynamic method dispatch
