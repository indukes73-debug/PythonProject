#Humandemo
class Human:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def speak(self,content):
        print(self.name+ ":"  + content)

h1 = Human("Indrayani",22)
h2 = Human("Shilpa",24)

h1.speak("Hi")
h2.speak("Hello")
h1.speak("How are you")

class Water_Bottle:
    def __init__(self, height,shape,company_name,storage,):
        self.height = height
        self.shape = shape
        self.company_name = company_name
        self.storage = storage

class Computer:
    def __init__(self, modal_name, price, size,colour,storage):
        self.modal_name = modal_name
        self.price = price
        self.size = size
        self.colour = colour
        self.storage = storage

class Bag:
    def __init__(self,size,colour,weight,price,type):
        self.name = size
        self.colour = colour
        self.weight = weight
        self.price = price
        self.type = type
class Chair:
    def __init__(self,type,size,length):
        self.size = size
        self.length = length
        self.type = type

class Animal:
    def __init__(self,name,type,brid,gender):
        self.name = name
        self.type = type
        self.brid = brid
        self.gender = gender
class Bird:
    def __init__(self,name,type,gender,brid,):
        self.name = name
        self.type = type
        self.gender = gender
        self.brid = brid

class Fruits:
    def __init__(self,name,colour,weight,category,taste):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.category = category
        self.taste = taste

class Flowers:
    def __init__(self,name,colour,category,):
        self.name = name
        self.colour = colour
        self.category = category

class Vegetables:
    def __init__(self,name,weight,price,type):
        self.name = name
        self.weight = weight
        self.price = price
        self.type = type

