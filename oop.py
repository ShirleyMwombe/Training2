
# class needed to create an object
# class - describes attributes and methods that a distinct object will have

from car import Car

car_1 = Car('Mitsubishi','Lancer',2020,'Grey')
car_2 = Car('Volkswagen','GTI',2020,'Black')

print(car_1.model)
print(car_2.make)

car_1.drive()
car_2.stop()

print(car_1.wheels)  # value is constant for each object

car_2.wheels = 2

print(car_2.wheels)  # changes the value of class variable for the specified object

Car.wheels = 6 # changes the value of the class variable for all the objects

print(car_1.wheels)