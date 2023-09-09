# EJERCICIO PRESTAMO WHILE ********************************

compra = int(input("Indique la cantidad a pagar: "))
ncuotas = int(input("Indique el total de cuotas del prestamo: "))

if compra != 0 and compra != '' and ncuotas != 0 and compra != '':
    cuota = int(compra / ncuotas)
    cuotan = 0

    while (ncuotas != 0):
        cuotan += 1
        print(f"Cuota #{cuotan}  pagar:{cuota} pesos" )
        ncuotas -=1
else:
    print("El valor o el número de cuotas debe ser superior a 0")
