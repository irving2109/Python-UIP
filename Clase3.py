import numpy as np
# Listas
# Las listas son arreglos
mi_lista = [1, 2, 3, 4]

# Para acceder a un elemento:
for i in mi_lista:
    print([i])
    
# Tuplas
# Son arreglos con datos inmutables
mi_tupla = (1, 2, 3, 4)

# Conjuntos
# Son arreglos con datos únicos
mi_conjunto = {1, 2, 3, 4}

# Diccionarios
# Son arreglos con formato clave-valor de cualquier tipo de dato
mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30,
}

# Matrices
# Son arreglos multidimensionales
# Se utiliza numpy
matriz = np.array([[1,2], [3,4]])

# Se puede trabajar con matrices de más de dos dimensiones

# Pilas
# Son arreglos con formato LIFO (Last In, First Out)
class Pila:
    def __init__(self):
        self.elementos = []
        # stack = []
    def apilar(self, elemento):
        self.elementos.append(elemento)
        
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
# Ejecución de la pila
""" pila = Pila()
pila.apilar(1)
pila.apilar(2)
print(pila.desapilar()) """

# Colas
# Son arreglos con formato FIFO (First In, First Out)
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, elemento):
        self.elementos.append(elemento)
        
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.popleft()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
# Ejecución de la cola
""" cola = Cola()
cola.encolar(1)
cola.encolar(2)
print(cola.desencolar()) """