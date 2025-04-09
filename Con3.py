usuario = input("USUARIO: ")
usuario = usuario.upper() #upper() es para pasarlo a mayuscula

if usuario == "DOCENTE":
    print ("Bienvenido: Docente.")
    password = input ("Contraseña: ".upper())
    if password.upper() == "ABC123":
        print("Usted es un usuario valido")
    else:
        print("Contraseña incorrecta")
else:
        print("Usuario incorrecto")