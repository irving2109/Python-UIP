from collections import deque

def es_subconjunto(a, b):
    cola = deque(a)
    while cola:
        elemento = cola.popleft()
        if elemento not in b:
            return False
    return True

# Ejemplo de uso:
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [1, 2, 3, 4, 5]

print("A es subconjunto de B:", es_subconjunto(A, B))
print("B es subconjunto de A:", es_subconjunto(B, A))