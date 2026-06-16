"""
    Una list comprehension combina el for loop
    y la creación de nuevos elementos en una sola
    línea y automáticamente agrega cada nuevo elementos
    a la lista, es decir, sin utilizar el append.
    
# 10 primeros números cuadráticos
print("\nLista de cuadrados")
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

"""
squares = [ value**2 for value in range(1,11) if value <= 5]
print(squares)

### SLICING A LIST
players = ["charly", "martina", "florence", "eli"]
#             0          1          2          3
print("\nLista original")
print(players)
#slicing de los primeros 3
print("Slice de los primeros 3")

print(players[0:2]) # Esto va a a imprimir desde el índice 0 hasta el 1

print(players[1:4]) # Esto va a imprimir desde el índice 1 hasta el 3

print("Slicing -1 ") # También puedo utilizar índices negativos para el slicing
print(players[-4:-1]) # Esto va a imprimir desde el inicio hasta el índice 2 

print(players[2:]) # Esto va a imprimir desde el índice 2 hasta el último

# Manera incorrecta de copiar una lista
players_1 = players

# Manera correcta de copiar una lista utilizando slicing
players_2 = players[:]

# Otra manera de copiar una lista utilizando un método de las listas
players_3 = players.copy()

# Otra manera de copiar una lista utilizando el método build-in list
players_4 = list(players)