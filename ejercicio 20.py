def calcular_can(monto):
    nominaciones = [500,200,100,50,20,10]
    monedas = 0

    for i in range(len(nominaciones)):
        nominacion = nominaciones[i]

        monedas += monto / nominacion
        monto = monto % nominacion

    return monedas 

print(calcular_can(1000))





