from operator import truediv


class Bank:
    def interest_rate(self):
        print("Interest Rate : 8% ")
        return 8

    def home_loan(self):
        print("Home Loan Available")
        return True

    def car_loan(self):
        print("Car Loan Available")
        return True

b1 = Bank()
b1.interest_rate()
b1.home_loan()
b1.car_loan()

print("======")


class HDFC(Bank):
    def interest_rate(self):
        print("HDFC Interest Rate : 3% ") #print statement is for display
        return 3# return statement is for data

    def home_loan(self):
        print("HDFC Home Loan Available")
        return True
    def car_loan(self):
        print("HDFC Car Loan Not Available")
        return False
h1 = HDFC()
h1.interest_rate()
h1.home_loan()
h1.car_loan()

print("======")


class ICICI(Bank):
    def interest_rate(self):
        print("ICICI Interest Rate : 4% ")
        return 4
    def home_loan(self):
        print("ICICI Home Loan Not Available")
        return False
    def car_loan(self):
        print("ICICI Car Loan  Available")
        return True
c1 = ICICI()
c1.interest_rate()
c1.home_loan()
c1.car_loan()

print("======")

class SBI(Bank):
    def interest_rate(self):
        print("SBI Interest Rate : 6% ")
        return 6
    def home_loan(self):
        print("Home Loan Not Available")
        return False
    def car_loan(self):
        print("Car Loan Not Available")
        return False
s1 = SBI()
s1.interest_rate()
s1.home_loan()
s1.car_loan()




