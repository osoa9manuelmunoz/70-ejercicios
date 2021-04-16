from math import sqrt

x1 = float(input("Digite el punto en x  : "))
y1 = float(input("Digite el punto en y  : "))
x2 = float(input("Digite el punto en x  : "))
y2 = float(input("Digite el punto en y  : "))

dis = sqrt((x1 - x2)**2 + (y1 - y2)**2)

print("la distancia es de: ",dis)