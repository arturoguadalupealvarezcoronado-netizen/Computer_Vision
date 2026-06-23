"""
    Estructura de un while loop en Python

    while conditional:
        while_actions
"""
# While con centinela
## Sumatoria de números hasta que el usuario 
## decida cuando parar
total = 0.0
while True:
    user_input = input("Ingresa un valor para sumar o 'q' para salir: ")
    try: 
        valor = float(user_input)
        total += valor # Estructura Acumuladora
    except ValueError:
        print("La conversión no se pudo realizar")

    # Centinela
    if user_input == "q":
        break

message = f"""
    Total aculumado {total}
    Fin del programa
"""

print(message)