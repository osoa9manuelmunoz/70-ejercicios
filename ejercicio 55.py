divisores = 0
n = int(input("ingrese un numero: "))
for i in range (1,n + 1):
    if n % i == 0:
        divisores +=1
print("la cantidad de divesores son: ",divisores)

    



