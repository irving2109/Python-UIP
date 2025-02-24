class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        if not self.contiene(valor):  # Evitar duplicados
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def contiene(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def mostrar(self):
        nodo_actual = self.cabeza
        elementos = []
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return elementos

def union_lista(a, b):
    conjunto_union = ListaEnlazada()
    for elemento in a:
        conjunto_union.agregar(elemento)
    for elemento in b:
        conjunto_union.agregar(elemento)
    return conjunto_union.mostrar()

def interseccion_lista(a, b):
    conjunto_interseccion = ListaEnlazada()
    for elemento in a:
        if elemento in b:
            conjunto_interseccion.agregar(elemento)
    return conjunto_interseccion.mostrar()

def diferencia_lista(a, b):
    conjunto_diferencia = ListaEnlazada()
    for elemento in a:
        if elemento not in b:
            conjunto_diferencia.agregar(elemento)
    return conjunto_diferencia.mostrar()

# Ejemplo de uso:
A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

print("Unión A ∪ B (Lista Enlazada):", union_lista(A, B))
print("Intersección A ∩ B (Lista Enlazada):", interseccion_lista(A, B))
print("Diferencia A - B (Lista Enlazada):", diferencia_lista(A, B))
