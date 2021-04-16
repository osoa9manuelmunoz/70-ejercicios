nombre =input("ingrese su nombre de usuario porfavor: ")
clave = int(input("ingrese su clave porfavor: "))

if clave == 1234:
    print("vienvenido señor {} que deseas hacer el dia de hoy".format(nombre))
else:
    print("el usuario deve estar incorecto o la contraseña porfa vuelve intenta")
