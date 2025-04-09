#José Nahúm Espinoza Solano
#Fecha de creación: 09/04/2025


from estudiante import Estudiante
from funciones import mostrar_menu, validar_edad, buscar_estudiante

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
