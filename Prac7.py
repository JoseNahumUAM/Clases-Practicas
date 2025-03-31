#7. Calcular el total a pagar por la compra de articulos en una tienda. Se
# sabe que el impuesto que se aplica es el 10% y se realiza un descuento
# del 5% sobre la compra

compra = float(input("Ingrese el total de su compra: "))
impuesto = compra * 0.15
descuento = compra * 0.05

total = compra + descuento - impuesto

print("El total a pagar es: ", total)
