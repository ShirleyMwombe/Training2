
class Car:
    # attributes

    wheels = 4  # class variable
    def __init__(self,make,model,year,colour):  # construct/create objects
        self.make = make  # instance variables
        self.model = model  # instance variables
        self.year = year  # instance variable = declared inside a contructor
        self.colour = colour

    # methods
    def drive(self):
        print('This ' +self.model+' is driving')
    def stop(self):
        print('This ' +self.model+' is stopped')
