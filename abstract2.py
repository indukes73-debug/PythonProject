from abc import ABC, abstractmethod

class Laptop(ABC):#we can"t make object of abstract class
    @abstractmethod
    def getName(self):
        pass

class Dell(Laptop):
    def getName(self):
        return "Dell"

    def os(self):
        return "Windows"

l1 = Dell()
print(l1.getName())
print(l1.os())

class HP(Laptop):
    def getName(self):
        return "HP"
    def os(self):
        return ("Linux")

l2 = HP()
print(l2.getName())
print(l2.os())