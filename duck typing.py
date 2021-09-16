# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present

class Duck:
    def walk(self):
        print('This duck is walking')

    def talk(self):
        print('This duck is talking')

class Chicken:
    def walk(self):
        print('This chicken is walking')

    def talk(self):
        print('This chicken is talking')

class Person:
    def catch(self,duck):
        duck.walk()  # from Duck class
        duck.talk()  # from Duck class
        print('You caught the bird!')

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)  # duck object as argument
person.catch(chicken)  # chicken object accepted in Duck method because it's class has the minimum methods called