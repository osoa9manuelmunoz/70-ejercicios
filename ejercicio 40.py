n1=int(input("ingrese el numero 1: "))
n2=int(input("ingrese el numero 2: "))
n3=int(input("ingrese el numero 3: "))
if n1 == n2 == n3:
    print("losiento solo puede pasar que dos numeros sean iguales no los tres")
elif n1 == n2:
    print("son iguales los numeros 1 y el 2")
elif n2 == n3:
    print("son iguales los numeros 2 y el 3")
elif n1 == n3:
    print("son iguales los numeros 1 y 3")
