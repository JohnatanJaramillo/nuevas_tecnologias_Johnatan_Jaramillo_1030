# Las listas son estructuras de datos lineales
# Se cren usando bkackes ej: my_list = [1,2]
# Las listas son ordenadas, esto quiere decir que el ultimo dato ingresado ocupará la ultima posisicón
# Emplea métodos para manipular los items de la misma.
# Como los array, la primera posición inicia en 0
# Permite items duplicados
# Las listas son mutables, es deceir podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos

nombres = ["Luis", "Andres", "Juan", "Maria", "Pedro"]
edad = [25,19,21,33,40]
estatura = [1.80, 1.65, 1.74, 1.66, 1.54]
casado = [False, False, False, True, True]
usuario = ["Pepito", 25 , 1.80, False]

print(nombres[0], edad[0], estatura[0], casado[0], usuario[0])

print(len(edad))

print(type(nombres))
print(type(edad))
print(type(estatura))
print(type(casado))
print(type(usuario))

# Slice --- Rangos en la lista ---

print(usuario[0:3])
# Imprime todo el rango menos lo que este en la posición 3

# Podemos validar si existe en la lista algun elemento

if "Pepito" in nombres:
    print(f"El nombre {nombres[0]} esta en la lista")
else:
    print("NO se encontró el nombre buscado")

nombres[0:3] = "Luis", "Pablo", "Pipe"
print(nombres[0:5]) 

# Queremos insertar un item en una posición especifica => insert(i,value)
nombres.insert(0,"Pepito")

# Podemos agregar items al final de la lista con append()
nombres.append("Laura")
print(nombres[0: ])

nombres2 = ["Lis", "Ana"]

listapureba = nombres.extend(nombres2)
print(nombres[0:])
print(type(listapureba))

nombres.remove("Lis")
print(nombres[0:])

nombres.pop(4)
print(nombres[0:])

del nombres[1]
print(nombres[0:])

nombres.clear()
print(nombres[0:])

# Recorrer Listas

for i in edad:
    print(i)

# Iterar en los index

for i in range(len(estatura)):
    print(estatura[i])

# Iterar la lista  usando While

i = 0

while i < len(usuario):
    print(usuario[i])
    i += 1

# List Comprenhensions

print("---------------------")
[print(x) for x in usuario]
print("---------------------")
for i, edades in enumerate(edad):
    print(i, edades)

labels = ["Id", "Name", "Last_name", "email", "password"]
usuario = {"1","Pepito", "Perez","pepito@gmail.com","xyz123"}

for i in range(len(usuario)):
    print(usuario[i])