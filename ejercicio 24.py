m = 0.19
precio = float(input("Digite el precio: "))

iva = precio * m
precio_total = precio + iva

print("el valor del producto sin IVA es de: ",precio)
print("el IVA es de: ",m)
print("el precio con iva es de: ",precio_total)

if precio > 150.000:
    descuento = precio * 0.15
    precio_final = precio - descuento 

print("con el descuento del 15% mayor a 150.000 sera: ",precio_final)