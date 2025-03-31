numero = int(input("Ingresa un número de tres cifras: "))

# Validación para asegurarnos que sea de 3 cifras
while numero < 100 or numero > 999:
    numero = int(input("Número inválido. Ingresa un número de tres cifras: "))

# Invertir el número
original = numero
reverso = 0

while numero > 0:
    digito = numero % 10
    reverso = reverso * 10 + digito
    numero = numero // 10

# Verificar si es igual al reverso
if original == reverso:
    print("El número es igual a su reverso.")
else:
    print("El número NO es igual a su reverso.")