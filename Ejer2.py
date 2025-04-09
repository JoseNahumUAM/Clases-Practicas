""""
Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado, 
del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad),
 es mayor de 1000, se aplicará un descuento del 12%.
"""

while True:
    n= input("Si quieres empezar escribe (Comnzar) y para salir (Terminar)")
    if n== "Terminar":
        print("Usted ya salio")
        break
    if n == "Comenza":
        Producto = float(input("Ingrese el precio del articulo: "))
        IVA = Producto * 0.15

        if Producto > 1000:
            Descuento = Producto * 0.12
            
        else:
            Descuento = 0
            
        Total = (Producto + Descuento) - IVA

        print("El total a pagar es de: ", Total)
