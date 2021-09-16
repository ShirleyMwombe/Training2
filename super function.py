# super() = Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used
#                  Common methods defined in parent class

class Shapes:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Shapes):
    def __init__(self,length,width):
        #self.length = length  #replaced w/ super function
        #self.width = width
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Shapes):
    def __init__(self,length,width,height):
        #self.length = length  # replaced w/ super function
        #self.width = width  # replaced w/ super function
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(5,5)
cube = Cube(4,6,3)

print(square.area())
print(cube.volume())
