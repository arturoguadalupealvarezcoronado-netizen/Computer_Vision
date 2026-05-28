"""
   Un string es de manera sencilla una serie de caracteres.
   En Python todo lo que se encuentre dentro de comillas 
   simples '' o comillas dobles "" es considerado un string.

   "Esto es un string"
   'esto también es un string'
   'Le dije a un amigo, "¡Python es mi lenguaje favorito!"'
   "El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpiente"

"""

subject_name = "clase de programación"
print("variable original")
print(subject_name)
print("title")
print(subject_name.title())

"""
   Un método es una acción que Python puede realizar en un fragmento de datos
   o sobre una variable.
   El punto (.) después de una varible seguido del
   método (palabra) title() dice que se tiene que ejecutar el
   método title() de la variable subject_name.

   Todos los métodos van seguido de paréntesis 
   porque en ocasiones necesitan información adicional
   para funcionar, lo cual iría dentro de los paréntesis.
   En esta ocasión el método .title() no requiere información
   adicional para ejecutarse.

"""
print("Método upper")
print(subject_name.upper()) #Convierte a mayúsculas todas las letras
print("Método lower")
print(subject_name.lower()) #convierte a minúsculas todas las letras

"""
   Concatenación o combinación de strings 
"""
print("\n\n")
print("Concatenación de string")
first_name = "Arturo"
last_name = "Alvarez"
full_name = first_name + " " + last_name
print (full_name)
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print("Hola, " + full_name.title() + "!")


message = "Hola, " + full_name.title() + "!"
print(message)


"""
Whitespaces

   Se refiere a cualquier caracter que no se imprime, es decir, un espacio,
   tabuladores y finales de linea. Los whitespaces se utilizan comúnmente 
   para organizar las salidas, del tal manera que sean más amigables 
   de leer o ver para los usuarios
"""
#Tabulador
print("WHITESPACES")
print("Python")
print("\tPython")

# Saldo de linea o final del linea
print("Lenguages: \nPython\nC\nJavascript")