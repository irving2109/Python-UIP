class ColaArregloDinamico:
    def __init__(self):
        self.cola = []

    # enqueue(x): Agregar un elemento al final de la cola
    def enque(self, x):
        self.cola.append(x)
        print(f"\nElemento {x} agregado a la cola.")

    # dequeue(): Sacar el elemento en la parte frontal de la cola
    def deque(self):
        if self.esta_vacia():
            print("\nLa cola está vacía. No se puede hacer deque.")
            return None
        elemento = self.cola.pop(0)
        print(f"\nElemento {elemento} sacado de la cola.")
        return elemento

    # front(): Obtener el elemento en la parte frontal sin eliminarlo
    def front(self):
        if self.esta_vacia():
            print("\nLa cola está vacía.")
            return None
        print(f"\nEl elemento en la parte frontal es: {self.cola[0]}")
        return self.cola[0]

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.cola) == 0

    # Mostrar todos los elementos de la cola
    def mostrar_cola(self):
        print("\nCola actual:")
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            for elemento in self.cola:
                print(elemento, end=" -> ")
            print("None")

# Ejemplo de uso:
cola = ColaArregloDinamico()

# Operaciones en la cola
cola.enque(10)
cola.enque(20)
cola.enque(30)

cola.mostrar_cola()

cola.front()

cola.deque()
cola.mostrar_cola()

cola.front()

cola.deque()
cola.deque()
cola.deque()  # Intento de dequeue en cola vacía