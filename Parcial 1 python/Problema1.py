from collections import deque

def max_subarray_sum(arr):
    suma_maxima = float('-inf')  # Inicializa con el valor más pequeño posible
    suma_actual = 0
    cola = deque()

    for num in arr:
        suma_actual += num
        cola.append(num)

        # Si la suma actual es mayor que la suma máxima, se actualiza
        suma_maxima = max(suma_maxima, suma_actual)

        # Si la suma actual es negativa, se reinicia la suma y la cola
        if suma_actual < 0:
            suma_actual = 0
            cola.clear()

    return suma_maxima

# Ejemplo de uso:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("La suma máxima del subarreglo es:", max_subarray_sum(arr))
