class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nodo al inicio
    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"\nNodo con valor {valor} insertado al inicio.")

    # Insertar un nodo al final
    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
        print(f"\nNodo con valor {valor} insertado al final.")

    # Buscar un nodo por su valor
    def buscar_valor(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                print(f"\nEl nodo con valor {valor} fue encontrado.")
                return True
            nodo_actual = nodo_actual.siguiente
        print(f"\nEl nodo con valor {valor} no se encuentra en la lista.")
        return False

    # Eliminar un nodo por su valor
    def eliminar_valor(self, valor):
        nodo_actual = self.cabeza
        anterior = None

        while nodo_actual:
            if nodo_actual.valor == valor:
                if anterior is None:
                    self.cabeza = nodo_actual.siguiente
                else:
                    anterior.siguiente = nodo_actual.siguiente
                print(f"\nNodo con valor {valor} eliminado.")
                return
            anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        
        print(f"\nEl nodo con valor {valor} no se encuentra en la lista.")

    # Mostrar la lista enlazada
    def mostrar_lista(self):
        nodo_actual = self.cabeza
        print("\nLista enlazada:")
        if not nodo_actual:
            print("La lista está vacía.")
        else:
            while nodo_actual:
                print(nodo_actual.valor, end=" -> ")
                nodo_actual = nodo_actual.siguiente
            print("None")

# Ejemplo de uso:
lista = ListaEnlazada()

# Insertar nodos
lista.insertar_inicio(10)
lista.insertar_final(20)
lista.insertar_inicio(5)
lista.insertar_final(30)

# Mostrar lista
lista.mostrar_lista()

# Buscar nodos
lista.buscar_valor(20)
lista.buscar_valor(100)

# Eliminar nodos
lista.eliminar_valor(10)
lista.eliminar_valor(100)

# Mostrar lista final
lista.mostrar_lista()
