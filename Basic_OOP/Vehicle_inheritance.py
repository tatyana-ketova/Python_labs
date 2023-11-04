"""
Veichle Inheritance
Create a Python program that models a hierarchy of vehicles
 using inheritance. Start with a base class Vehicle, and then
 create two or more derived classes (e.g., Car, Bicycle, Motorcycle)
  that inherit from the Vehicle class. Each class should have specific
  attributes and methods related to the type of vehicle it represents.
1. Define the Vehicle base class with common attributes such as make,
 model, and year, and methods like start(), stop(), and fuel_up().
2. Create derived classes for different types of vehicles, e.g., Car,
 Bicycle, and Motorcycle. Each derived class should inherit from the
 Vehicle base class and add attributes and methods specific to that
 type of vehicle. For example, the Car class might have attributes
 like num_doors, and the Bicycle class could have attributes like num_gears.
3. Implement specific methods for each derived class. For instance,
 the Car class might have a method to honk the horn, and the Bicycle
 class could have a method to ring the bell.
4. Create instances of each vehicle type and demonstrate their
specific methods and attributes. For example, you can create a car,
 bicycle, and motorcycle, and call methods like start(), stop(),
 and their specific methods like honk_horn() or ring_bell().
"""

class Vehicle:
    def __init__(self,model, year):
        self.model = model
        self.year = year

    def start(self):
        print(self.model+ " start... vr....vr....vr.." )
        pass
    def stop(self):
        print(self.model + " stop... shhh.....")

    def fuel_up(self):
        print(self.model + " om....om...ful!!!!")

class Car(Vehicle):
    def __init__(self, model, year, num_doors):
        Vehicle.__init__(self, model, year)
        self.num_doors = num_doors

    def honkhorn(self):
        print( self.model + " bip bip")


class Bicycle(Vehicle):
    def __init__(self, model, year, num_gears):
        Vehicle.__init__(self,model,year)
        self.num_gears = num_gears

    def ringbell(self):
        print(self.model + " dzin dzin")

class Motorcycle(Vehicle):
    def __init__(self,model, year, cradle):
        Vehicle.__init__(self, model, year)
        self.cradle = cradle

    def honkhorn(self):
        print(self.model + " bio bip")


MyCar = Car("Tesla",2021, 4)
MyMotobike = Motorcycle('Breddy', 2018,"no")
MyBicycle = Bicycle('Cargo',2023,8)
MyCar.start()
MyCar.stop()
MyCar.fuel_up()
MyCar.honkhorn()
MyBicycle.start()
MyBicycle.stop()
MyBicycle.fuel_up()
MyBicycle.ringbell()
MyMotobike.start()
MyMotobike.stop()
MyMotobike.fuel_up()
MyMotobike.honkhorn()


