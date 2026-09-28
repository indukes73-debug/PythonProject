from abc import ABC, abstractmethod

class Bag(ABC):
    @abstractmethod
    def getName(self):
        pass


class Student_bag(Bag):
    def getName(self):
        return "This is students school bag"

    def Use(self):
        return "To carry books"

b1 = Student_bag()
print(b1.getName())
print(b1.Use())

class Luggage_bag(Bag):
    def getName(self):
        return "This is luggage bag"
    def Use(self):
        return "To carry luggage"

b2 = Luggage_bag()
print(b2.getName())
print(b2.Use())