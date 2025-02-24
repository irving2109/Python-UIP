from collections import deque

def insertion_sort(arr):
    cola = deque(arr)  # Convertimos el arreglo en una cola
    lista_ordenada = []  # Lista temporal para almacenar los números ordenados

    while cola:
        num = cola.popleft()  # Tomamos el primer número de la cola
        # Insertamos el número en la posición correcta en la lista ordenada
        i = 0
        while i < len(lista_ordenada) and lista_ordenada[i] < num:
            i += 1
        lista_ordenada.insert(i, num)

    return lista_ordenada

# Ejemplo de uso:
arr = [5, 2, 9, 1, 5, 6]
print("Arreglo ordenado:", insertion_sort(arr))