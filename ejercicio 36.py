numero = int(input("ingrese su numero: "))
conut = 0

if numero < 100000:
    while numero > 0:
        numero //= 10
        conut +=1
        print("los digitos del numero son: ",conut)
else:
    print("el numero ingresaso supera a 100000")


