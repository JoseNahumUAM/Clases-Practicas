"""1. Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista.
 El vehículo puede ser una bicicleta, una moto, un carro o un camión. 
 Para definir el conjunto de vehículos deben utilizar una estructura adecuada. 
 El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.
"""
num=0
while num!=4:

    print ("\n\nIngrese un numero dependiendo de su veiculo")
    print ("Si es bicicleta ingrese 1")
    print ("Si es moto o carro ingrese 2")
    print ("Si es camion ingrese 3")
    print("Para salir del programa escriba 4")
    num = int(input())

    if num == 1:
        print("Usted tiene que pagar 100 cordobas")
    elif num == 2:
        kilometro = int (input("Ingrese cuantos kilometros a recorrido: "))
        print ("Usted tiene que pagar: ", kilometro * 30)
    elif num == 3:
        kilometro = int (input("Ingrese cuantos kilometros a recorrido: "))
        peso = int (input("Ingrese cuantas toneladas lleva: "))
        k = kilometro * 30 
        tonelada = peso * 25
        total = k + tonelada
        print ("Usted tiene que pagar: ", total)
    elif num == 4:
        print("Hasta pronto !")
    else:
        print("Usted digito un mal numero")