from abc import ABC, abstractmethod #abc is package and ABC is abstract class

class Bank(ABC):
    @abstractmethod
    def getInterestRate(self):
        pass

class SBI(ABC):
    def getInterestRate(self):
        return 5
    def getprofit(self):
        return 4

class HDFC(ABC):
    def getInterestRate(self):
        return 6

    def getprofit(self):
        return 4


    def getABCD(self):
        return 5

d1 = HDFC()
print(d1.getInterestRate())
print(d1.getABCD())
print(d1.getprofit())

print("========")

d2 = SBI()
print(d2.getInterestRate())
print(d2.getprofit())

