from math import sqrt

a =int(input("ingrese el numero a: "))
b =int(input("ingrese el numero b: "))
c =int(input("ingrese el numero c: "))

de = b**2 - 4*a*c

if de < 0:
    print("no existe soluciones reales")
else:
    x_1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
    x_2 = -b - sqrt(b**2 - 4*a*c) / (2*a)
    print("salucion en x1",x_1)
    print("salucion en x2",x_2)
