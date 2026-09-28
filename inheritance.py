class Animal:
    def speak(self):
        print("I am an Animal")

#class Dog(Animal):#here dog inhertis the properties of animal
    pass

#a1 = Dog()
#a1 = Animal()
#a1.speak()

class cat(Animal):
    pass
p1 = cat()
p1.speak()

class Dog(Animal):
    def speak(self):#When child class override the properties of parent class i.e it defines new function so it is called function overriding
        print("I am a Dog")

a1 = Dog()
a1.speak()


