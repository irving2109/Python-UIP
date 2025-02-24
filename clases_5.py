class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)  
        if self.cabeza is None:  
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:  
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo  

    def eliminar(self, valor):
        # Case 1: The list is empty
        if self.cabeza is None:
            print("La lista está vacía")
            return False

        # Case 2: The value to delete is at the head of the list
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente  
            print(f"El nodo con valor {valor} ha sido eliminado")
            return True

        # Case 3: Searching for the value in the next nodes
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.valor == valor:  
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente  
                print(f"El nodo con valor {valor} ha sido eliminado")
                return True
            nodo_actual = nodo_actual.siguiente

        #Caso 4: El valor no se encuentra en la lista
        print(f"El nodo con valor {valor} no se encontró")
        return False  # Value not found

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True 
            nodo_actual = nodo_actual.siguiente
        return False

# Example Usage
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

lista.mostrar()

# Search for Values
print(lista.buscar(2))
print(lista.buscar(4))
print(lista.buscar(5))

# Attempt to Remove Nodes
lista.eliminar(3)
lista.mostrar()