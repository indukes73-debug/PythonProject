from abc import ABC, abstractmethod

class Animal_1(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(ABC):
    def speak(self):
        return "I am a Dog"


    def bark(self):
        return "I can bark"

d1 = Dog()
print(d1.speak())
print(d1.bark())

class Cat(Animal_1):
    def speak(self):
        return "I am a Cat"

    def meow(self):
        return "I can meow"

d2 = Cat()
print(d2.speak())
print(d2.meow())


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Audi(Car):
    def drive(self):
        return "I am an Audi"

    def park(self):
        return "I need a parking"

c1 = Audi()
print(c1.drive())
print(c1.park())

class Swift(Car):
    def drive(self):
        return "I am a Swift "

    def park(self):
        return "I need a parking"

c2 = Swift()
print(c2.drive())
print(c2.park())



