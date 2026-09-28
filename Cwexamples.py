#to print the largest and smallest among three numbers

# Num1 = int(input("Enter first number:"))
# Num2 = int(input("Enter second number:"))
# Num3 =int(input("Enter third number:"))
#
# nums = [Num1, Num2, Num3]
# print("Largest Number:", max(nums))
# print("Smallest Number:", min(nums))

a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
c=int(input("Enter another number: "))

if a > b and a > c:
    print("largest:",a)
elif b > a and b > c:
    print("largest:",b)
else:
    print("largest:",c)

if a <  b and a  < c:
    print("smallest:",a)
elif b < a and b < c:
    print("smallest:",b)
else:
    print("smallest:",c)
