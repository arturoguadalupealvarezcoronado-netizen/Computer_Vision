"""

    If Statement

    if condition:
        do something

    if conditionals:
        actions
    else:
        actions

"""
try:
    age = int(input("¿Cuál es tu edad?")) # Age es del tipo entero 
except:
    print("Ingresaste erroneamente tu edad")
a = -1

"""
    if-elif-else
"""

if age >= 18:
    print("Tu ya tienes edad para votar")
    print("¿Y afuiste a trámitar tu INE?")
elif age < 18 and age >= 0:
    print("Lo siento, eres demasiado joven para votar")

    print("Fin del programa")