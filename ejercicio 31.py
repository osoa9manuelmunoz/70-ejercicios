v = float(input("ingrese el valor del pasaje del avion: "))
r = float(input("ingrese cuanta distancia a recorrido: "))
d = int(input("cuantos dias se ospedo: "))
if r > 1000 and d > 7:
    descuento = v * 0.15
    precio_final = v - descuento 
    print("con el decuento del 15% el pasaje seria de: ",precio_final)
else:
    print("el precio del pasaje seria siendo el mismo",v)
