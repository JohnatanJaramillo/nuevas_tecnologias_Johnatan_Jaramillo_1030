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

# if age >= 17 and height >=150:
#     print("Puede ingresar a la atracción")

# if age >= 13 or height >=150:
#     print("Puede ingresar a la atracción")

# persona1 = "Estudiante"
# Persona2 = "Visistante"

# if persona1 == "Estudiante":
#     print("Bienvenido")

# pago = input("Desea proceder con el pago?")
# if pago == "Si" or pago == "si":
#     servicio = input("¿Desea incluir el servicio?")
#     if servicio == "Si" or servicio == "si":
#         print("El total de su cobro es de ######")
#     else:
#         print("El total de su cobro es de xxxxxx")
# else:
#     print("Saliendo.....")   


#SWITCH*************************************
# opc = 0

# if opc == 1:
#     print("Registro")
# elif opc == 2:
#     print("Login")
# elif opc == 3:
#     print("Salir")
# else:
#     print("Seleccione una opción valida")    

#JUEGO*******************************************
# import random
# vidas = 5
# puntos = 0

# while(vidas != 0):
#     num = random.randint(0, 9)
#     if num == 0:
#         vidas -= 1
#         print(f"Vidas: {vidas}")
#     else:
#         puntos += 1
#         print(f"Puntos: {puntos}")

# EJERCICIO PRESTAMO WHILE******************************

# compra = int(input("Ingrese el valor de su compra: "))
# ncuotas = int(input("A cuantas cuotas desea diferir la compra?: "))

# if (compra != 0 and compra != "") and (ncuotas != 0 and ncuotas != ""):
#     cuota = int(compra / ncuotas)
#     cuotan = 0
#     while ncuotas != 0:
#         cuotan += 1
#         print(f"Cuota No{cuotan}: $ {cuota}")
#         ncuotas -= 1
# else:
#     print("Ingresar un valor o numero de cuota diferente de 0")

# EJERCICIO PRESTAMO CON LOGIN****************************
import random

captcha = {
    "2 + 2 * 2": 6,
    "5 * 3 + 10": 25,
    "20 - 7 * 2": 6,
    "8 / 2 + 5": 9
}
captcha_aleatorio= random.choice(list(captcha.keys()))
usuario = [
    {"email":"jejo@gmail.com","password": "123456"}
]
inicio = 0
while inicio == 0:
    print("__BIENVENIDO__")
    print("")
    print("Elija una de las siguientes opciones: ")
    print("1. Registrarse.")
    print("2. Iniciar Sesión.")
    print("3. Salir.")
    opmenu1 = int(input("Ingrese su opción: "))
    
    if opmenu1 == 1:
        print("")
        email = input("Ingrese Correo: ") 
        password = input("Ingrese una contraseña: ")
        print("Resuelve el siguiente captcha:")
        print(captcha_aleatorio)
        respuesta_usuario = int(input("Ingrese su respuesta: "))
        respuesta_correcta = captcha[captcha_aleatorio]
        if respuesta_usuario == respuesta_correcta:
            print("Usuario registrado con exito")
            print("")
            nuevo_usuario = {"email": email,"password": password}
            usuario.append(nuevo_usuario)
        else:
            print("")
            print("Error")
            print("")
    elif opmenu1 == 2:
        print("___Login___")
        print("")
        email = input("Ingrese Correo: ") 
        password = input("Ingrese una contraseña: ")
        usuario_temporal = {"email": email,"password": password}
        
    elif opmenu1 == 3:
        print("Vuelva pronto")
        inicio = 1
    else:
        print("Ingrese una opción correcta")