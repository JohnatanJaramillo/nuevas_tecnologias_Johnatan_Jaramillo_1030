import random

# EJERCICIO UNION DE LOS EJERCICIOS ANTERIORES

captcha = {
    "2 + 2 * 2": 6,
    "5 * 3 + 10": 25,
    "20 - 7 * 2": 6,
    "8 / 2 + 5": 9
}
captcha_aleatorio= random.choice(list(captcha.keys()))
usuario = [
    {"email":"123@gmail","password": "a123456789"}
]

inicio = 0
while inicio == 0:
    print("_____BIENVENIDO_____")
    print("")
    print("Elija una de las siguientes opciones")
    print("1. Registro")
    print("2. login")
    opcion = int(input("Opción -> "))
    

    # 
    # REGISTRO
    # 

    if opcion == 1:
        print("")
        print("______Registro______")
        print("")

        email = input("Ingrese Correo o Telefono: ") 
        clave_comparar = email
        password = input("Ingrese una contraseña: ")

        print("Resuelve el siguiente captcha:")
        print(captcha_aleatorio)
        respuesta_usuario = int(input("Ingrese su respuesta: "))
        respuesta_correcta = captcha[captcha_aleatorio]


        if respuesta_usuario == respuesta_correcta:
            nuevo_usuario = [{"email/tel": email,"password": password}]
            if clave_comparar in nuevo_usuario and clave_comparar in usuario:
                valor1 = nuevo_usuario[clave_comparar]
                valor2 = usuario[clave_comparar]

                if valor1 == valor2:
                    print("El correo ya esta registrado en una cuenta")
                else:
                    usuario.append(nuevo_usuario)
                    print("Usuario registrado con exito")
                    print("")

        else:
            print("")
            print("___Error___")
            print("")

    if opcion == 2:

        print("")
        print("______Login______")
        print("")

        email = input("Ingrese Correo o Telefono: ") 
        password = input("Ingrese una contraseña: ")


        usuario_temporal = {"email/tel": email,"password": password}
        usuario.append(nuevo_usuario)

        

