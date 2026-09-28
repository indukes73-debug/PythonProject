import random

cardDictionary = {
    1 : "Heart Ikka", 2: "Heart 2" ,3: "Heart 3" ,4: "Heart 4" ,5: "Heart 5" ,6: "Heart 6" ,7: "Heart 7" ,8: "Heart 8" ,9: "Heart 9" ,10: "Heart 10" ,11: "Heart Jack" ,12: "Heart Queen" ,13: "Heart King",
14: "Spades Ikka", 15: "Spades 2", 16: "Spades 3", 17: "Spades 4", 18: "Spades 5", 19: "Spades 6", 20: "Spades 7", 21: "Spades 8", 22: "Spades 9", 23: "Spades 10", 24: "Spades Jack", 25: "Spades Queen", 26: "Spades King",27: "Diamond Ikka", 28: "Diamond 2", 29: "Diamond 3", 30: "Diamond 4", 31: "Diamond 5", 32: "Diamond 6", 33: "Diamond 7", 34: "Diamond 8", 35: "Diamond 9", 36: "Diamond 10", 37: "Diamond Jack", 38: "Diamond Queen", 39: "Diamond King",40: "Clubs Ikka", 41: "Clubs 2", 42: "Clubs 3", 43: "Clubs 4", 44: "Clubs 5", 45: "Clubs 6", 46: "Clubs 7", 47: "Clubs 8", 48: "Clubs 9", 49: "Clubs 10", 50: "Clubs Jack", 51: "Clubs Queen", 52: "Clubs King"
}
cardNumberList = []
for i in range (1,53):
    cardNumberList.append(i)

print(cardNumberList)
print("-------")

randomList = []
for i in range (1,53):
    randomIndex = random.randint(0,52-i)#how 52-i
    randomList.append(cardNumberList[randomIndex])
    cardNumberList.remove(cardNumberList[randomIndex])

print(randomList)
print(cardNumberList)#empty because randomNumbers picked from cardNumbersList added to randomList so removed from here

player1List = []
player2List = []
player3List = []
player4List = []

index = 1
for i in randomList:
    if index % 4 == 1:
        player1List.append(cardDictionary.get(i))
    elif index % 4 == 2:
        player2List.append(cardDictionary.get(i))
    elif index % 4 == 3:
        player3List.append(cardDictionary.get(i))
    else:
        player4List.append(cardDictionary.get(i))
        index = index + 1
print("player1List",player1List)
print("player2List",player2List)
print("player3List",player3List)
print("player4List",player4List)



