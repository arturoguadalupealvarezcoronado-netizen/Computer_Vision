"""
    Vamos a realizar un código que pida al usuario
    un PIN de acceso. 

    Si el usuario ingresa correctamente el PIN entonces el acceso es 
    concecido.

    Si el usuario ingresa incorrectamente el PIN entonces el programada
    debe decirle PIN incorrecto, ingresa PIN nuevamente

    Si el usuario ingresa incorrectamente el PIN más de 3 veces
    entonces el acceso será bloqueado
"""
PIN_OK = "1234" # CONSTANTE
INTENTOS_MAX = 3 # CONSTANTE
intentos = 0 # Variable

while intentos < INTENTOS_MAX:
    user_input = input("Ingresa tu PIN para acceder")
    if user_input == PIN_OK:
        print("Acceso concecido")

        message = """ 
                Bienvenido al sistema gestor de calificaciones.

            Charly Ingresar las calificacioens reprobatorias de tus alumnos.
        """
        print(message)

        break
    else:
        intentos+=1 # Estructura contadora
        restantes = INTENTOS_MAX - intentos # Intentos restantes
        if restantes > 0:
            print(f" PIN incorrecto, ingresa PIN nuevamente: Intentos restantes {restantes}")
        else:
            print("Intentos superados")
            print("Cuenta bloqueada")