#code to find maximum and minimum number in an array
ar = [10,20,5,17,45,12]

max = ar[0]
min = ar[0]

for i in ar:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"max: {max}, min: {min}")

