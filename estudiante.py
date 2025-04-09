# estudiante.py

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        """
        Inicializa un nuevo estudiante con nombre, edad, carrera y una lista vacía de calificaciones.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        """
        Agrega una calificación al estudiante si está dentro del rango 0-100.
        """
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
        else:
            print("La calificación debe estar entre 0 y 100.")

    def promedio(self):
        """
        Calcula y devuelve el promedio de las calificaciones del estudiante.
        """
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def mostrar_info(self):
        """
        Muestra toda la información del estudiante, incluyendo su promedio.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.promedio():.2f}")
