total = 0
numero = 1
contim = 0
pares = int(0)
sero = 0
while numero != 0:
    numero = int(input("ingrese un numero par (0 para terminar): "))
    total = total +1 
    if numero >= 0:
        sero = sero + 1
    else:
        print("solo numeros positivos") 
    if numero % 2==0:
        pares = pares + 1
    else:
         contim = contim + 1
print("los numeros positivos son",sero)
print("los numeros pares son",pares)
print("los numeros impares son",contim)
print("todos los numero ingresados son",total)
