st= {10,30,20,70,30,25}
print(st)
st.add(20)
print(st)
st.add(45)
print(st)
print(len(st))
print("------------")
for a in st:
 print(a)
print("-----")
import random #to take any random no its a package library in py
randomNumber = random.randint(1,100) #you have to give value from where to where you want mandatory
print(randomNumber)
print("---------")
#to take any random no its a package library in py
allNumbers={0} #a new variable

while True:
     randomNumber = random.randint(1,100)#if len is from 1 to 8 and you have gave len 10 so loop willgo infinite cause until the len is not fulfilled it will not brk
     print(randomNumber)
     allNumbers.add(randomNumber)
     print(allNumbers)
     if len(allNumbers) == 10:
         break
     print("All Numbers:",allNumbers)
print("---------")
import random
allNumbers = {0}

while True:
 randomNumber =random.randint(1,4)#as len (6) is less than len(1to 4)of random no loop will be infinite
 print(randomNumber)
 allNumbers.add(randomNumber)
 print(allNumbers)
 if len(allNumbers) == 6:
     break

print("ALL Numbers:",allNumbers)

