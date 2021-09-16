
class Car:
    colour = "Red"

def new_colour(car,colour):
    car.colour = colour

car_1= Car()
car_2= Car()
car_3= Car()


new_colour(car_1,"Grey")
new_colour(car_2,"Black")
new_colour(car_3,"Wine Red")


print(car_1.colour)
print(car_2.colour)
print(car_3.colour)