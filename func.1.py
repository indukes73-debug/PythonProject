def add(a,b):
    c = a+b
    return c

def printMyFullName(firstName,lastName = "Bhor"):
    print(f"Hello {firstName} {lastName}")

printMyFullName("Indrayani","Kapare") #Positional argument
printMyFullName("Kapare","Indrayani")#position changed

printMyFullName(lastName = "Kapare", firstName = "Indrayani")#keyword argument

printMyFullName("Indrayani")
printMyFullName("Sakshi")

def add(a,b,c=100 ,d=45):
    e = a+b+c+d
    return e
k = add(10,20,30)
print(k)
