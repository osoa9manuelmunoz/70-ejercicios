n1=int(input("ingrese el numero 1: "))
n2=int(input("ingrese el numero 2: "))
if n1 == n2:
    print("son iguales")
elif n1>n2:
    print("el numero mayor es: ",n1)
    print("el numero menor es: ",n2)
else:
    print("el numero mayor es: ",n2)
    print("el numero menor es: ",n1)