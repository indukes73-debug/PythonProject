class Bank:
    def __init__(self,bank_name,interest_rate):
        self.bank_name = bank_name
        self.interest_rate = interest_rate

    def home_loan(self, Loan_amount,time):
        interest = (Loan_amount*self.interest_rate*time)/100
        total = Loan_amount+interest
        print("total amount with interest :",total) #make compound interest same

b1 = Bank("Axis", 5)
b2 = Bank("HDFC", 8)

b1.home_loan(5000000,15)
b2.home_loan(10000000,13)

