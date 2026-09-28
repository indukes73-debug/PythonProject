#while
# a = 1
# while a < 10: #condition
#     print(a)
#     a=a+1
# #reverse
# a = 10
# while a > 0:
#     print(a)
#     a=a-1

# while

balance = 0
while True:
    print("=============================")
    print("Enter 1 for deposit")
    print("Enter 2 for withdraw")
    print("Enter 3 for statement")
    print("Enter 4 for Current Balance")
    print("Enter 5 for Exit")
    print("-----------------------------")
    choice = int(input("Please enter your choice: ")) #input from user
    if choice == 1:
        depositAmount = int(input("Enter your deposit amount : "))
        balance = balance + depositAmount
        print("Rs.",depositAmount, "/- amount added successfully.")
    elif choice == 2:
        withdrawAmount = int(input("Enter your withdraw amount : "))
        if balance >= withdrawAmount:
            balance = balance - withdrawAmount
            print("Rs.",withdrawAmount, "/- amount withdraw successfully.")
        else:
            print("Insufficient balance")
    elif choice == 3:
        print("You entered for statement")
    elif choice == 4:
        print("YOUR CURRENT BALANCE : Rs.", balance, " /-")
    elif choice == 5:
        break
    else:
        print("Please enter correct choice")



print("thanks for using my ATM. visit again")
