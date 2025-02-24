class PilaArregloDinamico:
    def __init__(self):
        self.pila = []

    # push(x): Agregar un elemento al tope de la pila
    def push(self, x):
        self.pila.append(x)
        print(f"\nElemento {x} agregado a la pila.")

    # pop(): Eliminar el elemento en el tope
    def pop(self):
        if self.esta_vacia():
            print("\nLa pila está vacía. No se puede hacer pop.")
            return None
        elemento = self.pila.pop()
        print(f"\nElemento {elemento} eliminado de la pila.")
        return elemento

    # top(): Obtener el elemento en el tope sin eliminarlo
    def top(self):
        if self.esta_vacia():
            print("\nLa pila está vacía.")
            return None
        print(f"\nEl elemento en el tope es: {self.pila[-1]}")
        return self.pila[-1]

    # Verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0

    # Mostrar todos los elementos de la pila
    def mostrar_pila(self):
        print("\nPila actual:")
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            for elemento in reversed(self.pila):  # Se muestra desde el tope hacia abajo
                print(elemento)

# Ejemplo de uso:
pila = PilaArregloDinamico()

# Operaciones en la pila
pila.push(10)
pila.push(20)
pila.push(30)

pila.mostrar_pila()

pila.top()

pila.pop()
pila.mostrar_pila()

pila.top()

pila.pop()
pila.pop()
pila.pop()  # Intento de pop en pila vacía