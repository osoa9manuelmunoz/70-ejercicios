n = int(input("ingrese un numero n: "))
m = int(input("ingrese un numero m: "))
total = 0
if n > m:
    print("m debe ser mayor que n")
while n <= m :
    total+=n
    n+=1
    print(n)
print("la suma del resultado total entre estos numeros es: ",total)