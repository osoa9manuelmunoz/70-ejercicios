
nota = 0

no1 = float(input("nota 1: "))
no2 = float(input("nota 2: "))
no3 = float(input("nota 3: "))
no4 = float(input("nota 4: "))
no5 = float(input("nota 5: "))
    
nota  = no1*0.15 + no2*0.2 + no3*0.15 + no4*0.3 + no5*0.2 
print("la nota final es: ", nota)
if (nota < 2.00):
    print ("el estudiante no puede abilitar")
elif(nota < 3.00):
    print("el estudiante reprobo la materia")
elif(nota >= 3.00)and(nota < 4.50):
    print("el estudiante aprobo la materia")
elif(nota >= 4.50):
    print("felicitaciones tienes un buen puntaje")
