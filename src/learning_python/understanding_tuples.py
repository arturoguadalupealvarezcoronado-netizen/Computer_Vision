"""
    TUPLAS
    
    Las tuplas son listas de elementos 
    que no cambian de tamaño. 
    
    Las tuplas son inmutables.
    
    Se utilizan los () para definir una tupla.
    
    Ejemplo.
        Si tenemos un rectángulo que siempre va a tener
        cierto tamaño, podemos asegurar que su tamaño 
        no va a cambiar si colocamos sus valores en una 
        tupla.
"""
dimensions = (200, 50) # Esto ya es una tupla
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 500

for dimension in dimensions:
    print(dimension)
    
"""
    No podemos modificar la tupla, lo que si podemos
    hacer es cambiar la asignación a una variable que 
    almacena una tupla.
"""
rectangle_dimension = (20, 15)
print(rectangle_dimension)
rectangle_dimension = (10, 5)
print(rectangle_dimension)