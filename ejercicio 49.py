pin = int(input("ingrese la cantidad de numeros que sumara: "))
suma=0
c=1
if pin<c:
    print("porfavor ingrese numeros positivos para haci lograr sumar")
while c<=pin:
    num = int(input("ingrese el numero para sumar: "))
    suma=suma+num
    c=c+1
    promedio=suma/c
print("el resultado de la suma es: ",suma)
print("el promedio es: ",promedio)