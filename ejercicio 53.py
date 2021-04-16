numero = 1
contim = int(0)
pares = int(0)
ocho = 0
sero=0
one=0
while numero != 0:
    numero = int(input("ingrese un numero (0 para terminar): "))
    if numero >= 0:
        sero = sero + 1
    else:
        one = one + 1
    if numero % 8==0:
        print("el numero es multiplo de 8: ",numero)
        ocho = ocho + 1
    if numero % 2==0:
        pares = pares + 1
    else:
        contim = contim + 1
print("los numeros positivos son",sero)
print("los numeros negativos son",one)
print("los numeros pares son",pares)
print("los numeros impares son",contim)
print("los numeros de multiplos de son",ocho)


