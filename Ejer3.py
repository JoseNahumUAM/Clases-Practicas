"""
3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% 
por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad 
del producto por cada docena en exceso sobre 3. Diseñe un programa que determine el monto de la compra, el monto del descuento, 
el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.
"""
while True:
    n= input("Si quieres empezar escribe (Comnzar) y para salir (Terminar)")
    if n == "Terminar":
        print("Usted ya salio")
        break
    if n == "Comenzar":
        Docena = int(input("Ingrese el total de docenas que va a comprar: "))
        Precio = int(input("Ingrese cuanto vale cada docena: "))
        Pago = Docena * Precio

        if Docena <= 3:
            Descuento = Pago * 0.10
        else:
            Descuento = Pago * 0.15
            Unidad = Docena

        total= Pago - Descuento
        print ("El pago por las docenas: ",Pago)
        print("El descuento es: ", Descuento)
        print("El total a pagar es: ",total )
        print("Las unidades regaladas son: ",Unidad)