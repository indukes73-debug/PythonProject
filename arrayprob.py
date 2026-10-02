rainfall = [12,24,7,56,1,10,94]

sum = 0
totaldays = 0
minFall = rainfall[0]
maxFall = rainfall[0]
for fall in rainfall:
    if fall > maxFall:
        maxFall = fall
    if fall < minFall:
        minFall = fall
    sum = sum + fall
    totaldays = totaldays + 1

avg = sum / totaldays
print(f"avg : {avg}")
print(f"min : {minFall}")
print(f"max : {maxFall}")

sorted_list = []

while rainfall:
    smallest = rainfall[0]
    for num in rainfall:
        if num < smallest:
            smallest = num
    sorted_list.append(smallest)
    rainfall.remove(smallest)

print(sorted_list)


