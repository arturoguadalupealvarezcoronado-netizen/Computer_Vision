"""
    Las listas también pueden almacenar números. 
    Python ofrece muchas herramientas 
    eficientemente con listas de números.
"""

#Método built-in range() - generador de números 
# El método range nos ayuda a crear fácilmente 
# series de números. Ejemplo:
# es cerrado por la izquierda y abierto por la derecha.
for value in range(1,6): # No contempla el 5,
    print(value) 
print(value)

# Como generamos una lisat con range 
numbers = list(range(1,5))
print(numbers)
print(len(numbers))

# Lista de números pares hasta el 100
print("\nNúmeros pares")
even_numbers = list(range(2, 101, 2))
print(even_numbers)

# Lista de números impares hasta el 100
print = ("\nNúmeros impares")
odd_numbers = list(range(2, 101, 2))
print(odd_numbers)


### Podemos crear cualquier lista de número utilizando 
# range, por ejemplo, hagamos una lista de los 
# 10 primeros números cuadráticos
print("\nLista de cuadrados")
squares = []
for value in range(1,11)
    square = value ** 2
    squares.append(square)
print(squares)

## Más métodos build-in 
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digits = list(range(1,11))
print(digits)
# Si quiero saber el mínimo de una lista de números
# utilizo el método build-in min
print(min(digits))

# Si quiero saber el máximo de una lista de números
# utilizo el método build-in  max
print(max(digits))

# Si quiero sumar los elementos de una lista utilizo sum
print(sum(digits))