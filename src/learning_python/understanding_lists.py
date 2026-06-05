"""
   Las listas nos permiten almacenar información 
   en un lugar, la cantidad que tengas: ya sean 
   pocos o millones de elementos.

   Una lista es una colección de items (elementos)
   que tienen un orden particular. Se pueden crear listas
   que incluyan strings, numeros, bolleanos, e incluso otras listas,
   etc, podemos almacenar lo que queramos en una lista.

   Se recomienda nombrar una variable tipo lista en plural.

   En Python los corchetes [] indican una lista, sus elementos
   se separan por comas.

"""
# Ejemplo de una lista
bicycles = ['trek', "giant", "specialized", "cannondale"]
print(bicycles)

# Accediendo a los elementos de una lista
"""
   Las listas son colecciones ordenadas. Se puede acceder
   a cualquier elemento de la lista diciéndole a Python
   la posición o índice del elemento deseado.

   Para obtener el valor deseado, escribe el nombre
   de la variable de la lista, seguido del índice 
   del elemento que deseas entre corchetes [].
   
"""
print(bicycles[0].upper()) # Imprime el primer elemento de la lista

# En Python, el índice de las listas siempre comienza en 0, no en 1.
print(bicycles[1]) # Imprime el segundo elemento de la lista.
print(bicycles[2]) # Imprime el tercer elemento de la lista.

# Accesando al último elemento de la lista.
print("Último elemento de la lista:")
print(bicycles[-1]) # Imprime el último elemento de la lista.
print(bicycles[-2]) # Imprime el penúltimo elemento de la lista.

# Utilizando valores individuales de una lista
message = "My first bicycles was a " + bicycles[1].title() + "."
print(message)

message_2 = f"My first bicycles was a {bicycles[1].title()}."
print(message_2)


## Agregar elementos a una lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print("\nMotocicletas: ")
print(motorcycles)

print("\n")
motorcycles.append("ducati")
print(motorcycles)

# Crear una lista vacía
motorcycles_2 = []
print("\nMotocicletas 2: ")
print(motorcycles_2)

motorcycles_2.append["honda"]
motorcycles_2.append["yamaha"]
motorcycles_2.append["suzuki"]
print(motorcycles_2)





# Eliminando elementos de una lista
# Método build-in del statement del
# Para utilizar el statement del
# pero debemos conocer el índice del elemento
# que deseamos eliminar
print("\nEliminando el 4to elemento de la lista: ")
print("Utilizando el statement del")
del motorcycles_2[3]
print(motorcycles_2)