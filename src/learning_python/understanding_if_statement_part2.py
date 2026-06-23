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
    age = int(input("¿Cuál es tu edad? ")) # Age es del tipo entero
except:
    print("Ingresaste erroneamente tu edad")
    age = -1

"""
    if-elif-else
"""

if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿Ya fuiste a tramitar tu INE?")
elif age < 18 and age >=0:
    print("Lo siento, eres demasiado joven para votar")
else:
    print("Error del usuario")

if age >= 18:
    print("Tu tienes la edad para votar")
    print("¿Ya fuiste a tramitar tu INE?")

if age < 18 and age >= 0:
    print("Lo siento, eres demasiado joven para votar")

if age < 0:
    print("Error del usuario")

print("Fin del programa")

### Multiple conditions if blocks
### Multiple conditions if-elif-else block

# Empty List - how to know if a list is empty?
# Using two lists - how to know if elements are in two lists?