notes = [100 ,50,20,10,2,1]

total_bill = int(input("Enter total amount: "))
amount_given = int(input("Enter amount given: "))
totalAmountToPayBack = amount_given - total_bill


def noteToGivenBack(totalAmountToPayBack):
    for note in notes:
        if (note <= totalAmountToPayBack):
            print(f"Note given : {note}")
            totalAmountToPayBack = totalAmountToPayBack - note
            break

    return totalAmountToPayBack

while totalAmountToPayBack != 0:
    totalAmountToPayBack = noteToGivenBack(totalAmountToPayBack)

