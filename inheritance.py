
class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')
    def sleep(self):
        print('This animal is sleeping')

class Rabbit(Animal):

    def run(self):
        print('This rabbit can run')

class Cat(Animal):
    def purr(self):
        print('This cat can purr')
class Dog(Animal):
    def bark(self):
        print('This dog can bark')

rabbit = Rabbit()
cat = Cat()
dog = Dog()

#print(rabbit.alive)
#at.eat()
#dog.sleep()

rabbit.run()
cat.purr()
dog.bark()