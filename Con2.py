# Descuento

precio = float(input("Escribe el precio: "))
if precio <= 1000:
    desc = precio * 0.1

print("El total a pagar es: ", precio - desc)