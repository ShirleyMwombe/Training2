#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.
# all parent abstract methods must be implemented in the child classes

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child

from abc import ABC, abstractmethod  # abc(abstract base class)


class Vehicle(ABC):

    @abstractmethod
    def go(self):  # abstract method
        pass


class Car(Vehicle):
    def go(self):
        print('Drive the car')


class Motorcycle(Vehicle):
    #def go(self):
     #   print('Ride the motorcycle')
     pass  # will inherit go method from vehicle, object cannot be created, compelled to override abstract method


#vehicle = Vehicle()  # object cannot be created from abstract class
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
