n1=int(input("ingrese el numero 1: "))
n2=int(input("ingrese el numero 2: "))
n3=int(input("ingrese el numero 3: "))

if n2 < n1 > n3:
    print("el primer numero es el  mayor: ",n1)
elif n1 < n2 > n3:
    print("el segundo numero es el mayor: ",n2)
elif n1 < n3 > n2:
    print("el tercer numero es el mayor: ",n3)

if n2 > n1 < n3:
    print("el primer numero es el menor: ",n1)
elif n1 > n2 < n3:
    print("el segundo numero es el menor: ",n2)
elif n1 > n3 < n2:
    print("el tercer numero es el menor:  ",n3)

 