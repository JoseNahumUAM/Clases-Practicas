# funciones.py

from estudiante import Estudiante

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
