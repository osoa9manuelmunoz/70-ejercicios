n1=int(input("ingrese el numero 1: "))
n2=int(input("ingrese el numero 2: "))
n3=int(input("ingrese el numero 3: "))

if n2 < n1 > n3:
    print("se esta disminuyendo {},{},{}".format(n1,n2,n3))
elif n1 < n2 > n3:
    print("ni se incrementa ni se desminuye{},{},{}".format(n1,n2,n3))
elif n1 < n3 > n2:
    print("se esta incrementando {},{},{}".format(n1,n2,n3))
