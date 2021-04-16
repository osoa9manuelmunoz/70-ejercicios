A = float(input("Digite la aceleracion del objeto en m/s: "))
T = float(input("Digite el tiempo del objeto en segundos: "))
V = float(input("Digite la velocidad inicial del objecto en /S: "))

X = (V*T)+(1/2*A*(T**2)) 
print("la distancia recorrida es de: ",X)