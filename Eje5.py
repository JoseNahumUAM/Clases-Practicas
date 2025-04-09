import math

def mostrar_menu():
    print("\n--- CÁLCULO DE ÁREAS ---")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Trapecio")

# Bucle principal
continuar = "s"

while continuar.lower() == "s":
    mostrar_menu()
    
    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print(f"Área del cuadrado: {area:.2f}")

    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"Área del rectángulo: {area:.2f}")

    elif opcion == 3:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * radio ** 2
        print(f"Área del círculo: {area:.2f}")

    elif opcion == 4:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"Área del triángulo: {area:.2f}")

    elif opcion == 5:
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        area = ((base_mayor + base_menor) * altura) / 2
        print(f"Área del trapecio: {area:.2f}")

    else:
        print("Opción inválida. Por favor, elija un número del 1 al 5.")

    continuar = input("\n¿Desea calcular otra área? (s/n): ")

print("¡Gracias por usar el programa!")