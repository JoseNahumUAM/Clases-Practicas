import FuncionesModulos
from FuncionesModulos import producto, division #Solo agarra esto

print("Ejemplificando funciones")
num1 = int(input("Escriba un número"))
num2 = int(input("Escriba otro número"))


print("La suma es: ",FuncionesModulos.sumar(num1,num2))
print("La resta es: ",FuncionesModulos.resta(num1,num2))
print("La resta es: ", producto(num1,num2))
print("La resta es: ", division(num1,num2))