# marks = [ 10,20,40,10,5,68,23]
# print(marks)
# print("-----")
# print(marks[1])
# print("-----")
# print(len(marks))
# print("-----")
# #print(marks[7])#error list index out of range
# #
# #
marks = [ 10,20,40,10,5,68,23]
a=0
while a<len(marks):
     print(marks[a])
     a=a+1
     print(a)

marks = []
while True:
     data = input ("Enter your data:")
     marks.append(data)  #append function to add data in your list at end
     print(marks)