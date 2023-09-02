

# Esto es definir la función

def saludar():
    print("Hola")

# Luego hacemos el llamado de la función

saludar()

# Funciones que reciben argumentos

def saludar2(name):
    print("Hola {name}")

# Hacemos el llamado de la función

saludar2("Maria")

# Cuando no conocemos el número de parametros que requiere la función

def imprimirLista(*args):
    print("Bienvenidos {args}")

imprimirLista("Pepito", "Luis", "Maria")

# Funciones con retorno:

def sumar(num1, num2):
    return num1 + num2

resultSuma = sumar(5,5)

print(resultSuma)

labels = ["Id", "Name", "Last_name", "email", "password"]
usuario = ["1","Pepito", "Perez","pepito@gmail.com","xyz123"]

def imprimirListas(lista):
    for i in range(len(usuario)):
        print(lista[i])

imprimirListas(usuario)
imprimirListas(labels)
