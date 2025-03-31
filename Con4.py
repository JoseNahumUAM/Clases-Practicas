

print ("Ingrese un numero dependiendo de su veiculo")
print ("Si es bicicleta ingrese 1")
print ("Si es moto o carro ingrese 2")
print ("Si es camion ingrese 3")
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
else:
    print("Usted digito un mal numero")
