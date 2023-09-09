import random
import re

# name = "Pepito"     #Esto es un String
# age = 17            #Esto es un entero
# note = 3.8          #Esto es un float
# isMarried = True    #Esto es un boolean
# b = b"Pepito"       #Esto es un byte

# print(name)
# print(age)
# print(note)
# print(isMarried)

# #Para conocer el tipo de dato podemos usar la función type()
# print(type(name))
# print(type(age))
# print(type(note))
# print(type(isMarried))

# age = 18
# height = 151

# if age >=17 and height >=150:
#     print("Puede ingresar a la atracción")



# if age >=13 or height >=150:
#     print("Puede ingresar a la atracción")





# person= "Estudiante"

# if person == "Estudiante":
#     print("Bienvenido al portal de estudiantes")
# else:
#     print("Registre su visita")

# valor: int = input("¿Cuál es el valor de su factura? ")
# pago = input(f'¿Desea pagar {valor}  pesos? ')

# if pago == "si":
#     print("Pagando")
#     servicio = input('¿Desea agregar el servicio? ')
#     if servicio == "si":
#         valor = valor (valor* 0.1)
#         print(f'El valor total a pagar es de {valor} pesos')
#     else:
#         print(f'El valor a pagar es de {valor} pesos')
# else:    
#     input("¿Desea hacer otro pago?")


captcha = {
    "2 + 2 * 2": 6,
    "5 * 3 + 10": 25,
    "20 - 7 * 2": 6,
    "8 / 2 + 5": 9
}
captcha_aleatorio= random.choice(list(captcha.keys()))
usuario = [
    {"email":"emmanuelq2005@gmail.com","password": "a123456789"}
]
print("_____BIENVENIDO_____")
print("")
print("______Login______")
print("")
email = input("Ingrese Correo o Telefono: ") 
password = input("Ingrese una contraseña: ")
print("Resuelve el siguiente captcha:")
print(captcha_aleatorio)
respuesta_usuario = int(input("Ingrese su respuesta: "))
respuesta_correcta = captcha[captcha_aleatorio]
if respuesta_usuario == respuesta_correcta:
    print("Usuario registrado con exito")
    print("")
    nuevo_usuario = {"email/tel": email,"password": password}
    usuario.append(nuevo_usuario)
else:
    print("Error")
for usuario in usuario:
    email = usuario["email/tel"]
    contraseña = usuario["password"] 
  