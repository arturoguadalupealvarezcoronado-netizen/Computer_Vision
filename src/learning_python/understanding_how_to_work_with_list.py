"""
   Trabajando con listas en Python

   Vamos a aprender como recorrer una lista
   sin importar el tamaño que tenga.

"""
magicians = ("ron", "harry", "hermione", "dumbledore", "snape", "draco")
print("Cuántos elementos tiene magician?")
print(len(magicians))

print(magicians(2))
print(magicians(5))
print(magicians(-1))

print("Hola" + magicians[0].title + ", eres una gran mago!")
print("Hola" + magicians[1].title + ", eres una gran mago!")
print("Hola" + magicians[2].title + ", eres una gran mago!")
print("Hola" + magicians[3].title + ", eres una gran mago!")
print("Hola" + magicians[4].title + ", eres una gran mago!")
print("Hola" + magicians[5].title + ", eres una gran mago!")

"""
   Lo anterior yo lo puedo reemplazar por un for
"""
print("\nAhora con un for:")
for magician in magicians:
    print("Hola " + magician.title() + ", eres un gran mago!")


"""
   # Looping

   for cat in cats:
   
   for dog in dogs:
   
   for item in list_of_items:
   
"""

# Vamos a imprimir un mensaje para cada mago
# magicians = ["ron", "harry", "hermione", "dumbledore", "snape", "draco"]
print("\nSaludo a magos")
for magician in magicians:
    print(magician.title() + "ese fue un gran hechizo")
    print(f"No puedo esperar para ver tu siguiente hechizo, + {magician.upper()}")
print("Gracias a todos, fue un gran espectáculo.")


###### IDENTACIÓN ######
"""
    Python utiliza la identación para determinar
    cuando una línea de código está conectada a 
    la línea de código anterior.
    
    Básicamente, se utilizan 4 espacios en blanco 
    para obligarnos a escribir código ordenado 
    y estructurado.
"""

"""
    No olvidemos identar
"""
magicians_2 = ["alice", "david", "carolina"]
for magician in magicians_2:
    print(magician)
    print(magician)
    print(magician)
    

# Identación innecesaria
message = "Hello Python world!"
#    print(message) - identación innecesaria
print(message)

# Olvidando los dos puntos
magicians_3 = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)