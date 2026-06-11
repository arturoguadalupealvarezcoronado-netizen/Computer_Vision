"""
   Una list comprehension combina el for loop 
   y la creación de nuevos elementos en una sola 
   línea y automáticamente


"""
squares = [value**2 for value in range(1,11)]
print(squares)

### SLICING A LIST
players = ["charly", "martina", "florence", "eli"]

print("\nLista original")
print("Players")
#slicing de los primeros 3
print("Slice de los primeros 3")
print(players[0:2]) # Esto va a imprimir desde el índice 0 hasta el 1

print(players[1:4]) #Esto va a imprimir desde el índice 1 hasta el 3

print("Slicing -1")
print(players[:3]) # Esto va a imprimir desde el inicio hasta el índice 2

print(players[2:]) # Esto va a imprimir desde el índice 2 hasta el último

# Manera incorrecta de copiar una lista
players_2 = players

# Manera correcta de copiar una lista
players_2 = players[:]

# Otra manera de copiar una lista 
players_3 = players.copy()

# Otra manera de copiar una lista 
players_4 = list(players)