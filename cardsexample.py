#To distribute 52 cards among 4 players randomly without repetition
import random
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
        player1List.append([i])
    elif index % 4 == 2:
        player2List.append(i)
    elif index % 4 == 3:
        player3List.append(i)
    else:
        player4List.append(i)
        index = index + 1
print("player1List",player1List)
print("player2List",player2List)
print("player3List",player3List)
print("player4List",player4List)



