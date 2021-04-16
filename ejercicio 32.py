a = int(input("Ingrese el año: "))
if a%4==0:
    if a%100 !=0 or a%400 ==0:
        print("el año es bisiesto")
    else:
        print("el año no es bisiesto")
else:
    print("el año no es bisiesto")