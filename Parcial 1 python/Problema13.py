from collections import deque

class ColaConDosPilas:
    def __init__(self):
        self.pila_entrada = deque()  # Pila para agregar elementos
        self.pila_salida = deque()   # Pila para sacar elementos

    # enqueue(x): Agregar un elemento al final de la cola
    def enqueue(self, x):
        self.pila_entrada.append(x)
        print(f"\nElemento {x} agregado a la cola.")

    # dequeue(): Sacar el elemento en la parte frontal de la cola
    def dequeue(self):
        if self.esta_vacia():
            print("\nLa cola está vacía. No se puede hacer dequeue.")
            return None
        # Si la pila de salida está vacía, pasar todos los elementos de la pila de entrada
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        elemento = self.pila_salida.pop()
        print(f"\nElemento {elemento} sacado de la cola.")
        return elemento

    # front(): Obtener el elemento en la parte frontal sin eliminarlo
    def front(self):
        if self.esta_vacia():
            print("\nLa cola está vacía.")
            return None
        # Si la pila de salida está vacía, pasar todos los elementos de la pila de entrada
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        print(f"\nEl elemento en la parte frontal es: {self.pila_salida[-1]}")
        return self.pila_salida[-1]

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.pila_entrada) == 0 and len(self.pila_salida) == 0

    # Mostrar todos los elementos de la cola
    def mostrar_cola(self):
        print("\nCola actual:")
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            elementos = list(self.pila_salida)[::-1] + list(self.pila_entrada)
            for elemento in elementos:
                print(elemento, end=" -> ")
            print("None")

# Ejemplo de uso:
cola = ColaConDosPilas()

# Llegan clientes a la fila
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

# Mostrar fila de clientes
cola.mostrar_cola()

# Atender a los clientes
cola.dequeue()
cola.mostrar_cola()

cola.front()

cola.dequeue()
cola.dequeue()
cola.dequeue()  # Intento de dequeue en cola vacía
