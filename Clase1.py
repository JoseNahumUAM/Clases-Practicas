# Vamos a ejemplificar una clases en Python

class Alumno:
    def __init__ (self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, {self.nombre} tu edad es: {self.edad}")
    
alumno = Alumno(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
alumno.saludar()
# Alumno.saludar(alumno) #Es otra forma