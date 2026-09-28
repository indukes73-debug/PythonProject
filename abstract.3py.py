from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getName(self):
        pass

class Circle(Shape):

    def getName(self):
        return "Circle"

    def vertex(self):
        return "0"
    def edges(self):
        return "0"

s1 = Circle()
print(s1.getName())
print (s1.vertex())
print(s1.edges())

class Rectangle(Shape):
    def getName(self):
        return "Rectangle"

    def edges(self):
        return "4"

    def vertex(self):
        return "4"

s2 = Rectangle()
print(s2.getName())
print(s2.vertex())
print(s2.edges())



# class Bag(ABC):
#     @abstractmethod
#     def getName(self):
#         pass
#
# class Student_bag(Bag):
#     def getName(self):
#         return "This is students school bag"
#
#     def Use(self):
#         return "To carry books"
#
# b1 = Student_bag()
# print(b1.getName())
# print(b1.Use())
#
# class Luggage_bag(Bag):
#     def getName(self):
#         return "This is luggage bag"
#     def Use(self):
#         return "To carry luggage"
#
# b2 = Luggage_bag()
# print(b2.getName())
# print(b2.Use())