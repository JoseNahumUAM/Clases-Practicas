#José Nahúm Espinoza Solano
#Fecha de creación: 09/04/2025


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


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\nMenu de opciones:")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")


def validar_edad(edad):
    """
    Valida que la edad ingresada sea un número entero positivo.
    """
    try:
        edad = int(edad)
        if edad > 0:
            return edad
        else:
            print("La edad debe ser un número entero positivo.")
            return None
    except ValueError:
        print("Por favor, ingrese un número entero válido para la edad.")
        return None


def buscar_estudiante(estudiantes, nombre):
    """
    Busca un estudiante por nombre en la lista de estudiantes.
    """
    for estudiante in estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None


def main():
    estudiantes = []  # Lista donde se almacenarán los estudiantes registrados

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registrar un nuevo estudiante
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = None
            while edad is None:
                edad_input = input("Ingrese la edad del estudiante: ")
                edad = validar_edad(edad_input)
            carrera = input("Ingrese la carrera del estudiante: ")

            # Crear el estudiante y agregarlo a la lista
            estudiante = Estudiante(nombre, edad, carrera)
            estudiantes.append(estudiante)
            print(f"Estudiante {nombre} registrado exitosamente.")

        elif opcion == "2":
            # Agregar calificación a un estudiante
            nombre = input("Ingrese el nombre del estudiante para agregar calificación: ")
            estudiante = buscar_estudiante(estudiantes, nombre)

            if estudiante:
                try:
                    calificacion = float(input(f"Ingrese la calificación para {nombre}: "))
                    estudiante.agregar_calificacion(calificacion)
                    print(f"Calificación de {calificacion} agregada a {nombre}.")
                except ValueError:
                    print("La calificación debe ser un número.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            # Mostrar información de un estudiante
            nombre = input("Ingrese el nombre del estudiante para mostrar información: ")
            estudiante = buscar_estudiante(estudiantes, nombre)

            if estudiante:
                estudiante.mostrar_info()
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            # Mostrar todos los estudiantes
            if estudiantes:
                for estudiante in estudiantes:
                    estudiante.mostrar_info()
                    print("-" * 20)
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()
