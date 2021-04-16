resp ="si"
nota = 0
while(resp!="no") :
    no1 = float(input("nota 1: "))
    no2 = float(input("nota 2: "))
    no3 = float(input("nota 3: "))
    no4 = float(input("nota 4: "))
    no5 = float(input("nota 5: "))
    
    if (resp!="no"):
        nota  = no1*0.15 + no2*0.2 + no3*0.15 + no4*0.3 + no5*0.2 
        print("la nota final es: ", nota)
    if (nota > 3.00):
        print ("el estudiante aprobó la materia")
    else:
        print ("el estudiante no aprobó la materia")

    if (resp!="no"):
        print("Deseas continuar (si/no)?: ")
        resp=input()

input()