tup = (10,20,30,20,50,26,4)
print(tup[2])

for item in tup: #Advance for loop called as for in loop used to access large data sequentially
    print(item)
print("-----------")
maxvalue = tup[0] # u cant initiate with  0 as in min case it gives wrong op
for everyvalue in tup:
    if everyvalue > maxvalue:
        maxvalue = everyvalue
    print( maxvalue)

print("Final max value:" ,maxvalue)

minvalue = tup[0]
for everyvalue in tup:
     if everyvalue < minvalue:
         minvalue = everyvalue
     print(minvalue)
print("------")
print("Final Minimum value:",minvalue)

print("==========-")

tup = (-10,-20,-30,-30,-50,-26,-4)
print(tup)

maxvalue = tup[0]
for everyvalue in tup:
     if everyvalue > maxvalue:
         maxvalue = everyvalue
     print(maxvalue)
print("------")
print("Final Max value:",maxvalue)

minvalue = tup[0]
for everyvalue in tup:
     if everyvalue < minvalue:
         minvalue = everyvalue
         print(minvalue)
print("------")
print("Final Minimum value:",minvalue)

print("------")

print("=============")
tup = (4,78,45,-6,-21)
positive_value = tup[0]
negative_value = tup[0]
if positive_value > 0:
  print(positive_value)
else:
  print(negative_value)
