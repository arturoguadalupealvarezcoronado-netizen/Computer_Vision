# Variables
# Vamos a entender a las variables 
message = "This is my first program :), I am very happy"
another_message = "Really, really happy"
print(message)
print(another_message)
print(message, another_message)
print(another_message, message)


"""
Los nombres de vaariables deben nombrar solo con:
   - letras, numeros y guión baj.
   - deben comentar con una letra o guión bajo
       pero no con un número: message_1 (ok), 1_message(wrong)
   - No utilizar espacios para separar palabras en variables:
   first name (WRONG) first_name (ok)
   - No utilizar palabras reservadas en python o el nombre
    del archivo como nombre de variables
   - los nombres deben ser cortos, pero descriptivos 
   - letras en minúsculas, por ahora.
   - en inglés
"""

## TRACEBACK
message = "Hola amigo"
print(message)

"""
NameError: Olvidamos establecer el valor de una variable
antes de usarla o cometimos un error
al ingresar el nombre de una variable
"""