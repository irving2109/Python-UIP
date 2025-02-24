class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Insertar un nodo al final
    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:  # La lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        print(f"\nNodo con valor {valor} insertado al final.")

    # Mostrar la lista en orden
    def mostrar_lista(self):
        nodo_actual = self.cabeza
        print("\nLista enlazada en orden:")
        if not nodo_actual:
            print("La lista está vacía.")
        else:
            while nodo_actual:
                print(nodo_actual.valor, end=" <-> ")
                nodo_actual = nodo_actual.siguiente
            print("None")

    # Mostrar la lista en orden inverso
    def mostrar_lista_inversa(self):
        nodo_actual = self.cola
        print("\nLista enlazada en orden inverso:")
        if not nodo_actual:
            print("La lista está vacía.")
        else:
            while nodo_actual:
                print(nodo_actual.valor, end=" <-> ")
                nodo_actual = nodo_actual.anterior
            print("None")

    # Invertir la lista
    def invertir_lista(self):
        nodo_actual = self.cabeza
        temp = None
        while nodo_actual:
            # Intercambiar siguiente y anterior
            temp = nodo_actual.anterior
            nodo_actual.anterior = nodo_actual.siguiente
            nodo_actual.siguiente = temp
            # Avanzar al siguiente nodo (que ahora es el anterior)
            nodo_actual = nodo_actual.anterior
        
        # Intercambiar cabeza y cola
        if temp:
            self.cabeza, self.cola = self.cola, self.cabeza
        
        print("\nLa lista ha sido invertida.")

# Ejemplo de uso:
lista = ListaDoblementeEnlazada()

# Insertar nodos
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
lista.insertar_final(40)

# Mostrar lista en orden normal
lista.mostrar_lista()

# Mostrar lista en orden inverso
lista.mostrar_lista_inversa()

# Invertir lista
lista.invertir_lista()

# Mostrar lista invertida en orden normal
lista.mostrar_lista()

# Mostrar lista invertida en orden inverso
lista.mostrar_lista_inversa()
