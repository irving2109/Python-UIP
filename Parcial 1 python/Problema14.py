class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None


    # Agregar un nodo al final de la lista
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo


    # Crear un ciclo en la lista enlazada conectando el último nodo a 'pos'
    def crear_ciclo(self, pos):
        if pos < 0:
            return
        nodo_ciclo = None
        nodo_actual = self.cabeza
        contador = 0
        ultimo = None
        
        while nodo_actual:
            if contador == pos:
                nodo_ciclo = nodo_actual
            ultimo = nodo_actual
            nodo_actual = nodo_actual.siguiente
            contador += 1
        
        # Conectar el último nodo al nodo_ciclo
        if ultimo and nodo_ciclo:
            ultimo.siguiente = nodo_ciclo
            print(f"\nCiclo creado conectando el último nodo al nodo con valor {nodo_ciclo.valor}")



    # Detectar ciclo usando Algoritmo de Floyd (Tortuga y Liebre)
    def detectar_ciclo(self):
        tortuga = self.cabeza
        liebre = self.cabeza

        while liebre and liebre.siguiente:
            tortuga = tortuga.siguiente          # Mueve un paso
            liebre = liebre.siguiente.siguiente  # Mueve dos pasos

            if tortuga == liebre:
                print("\n¡Ciclo detectado! La lista tiene un ciclo.")
                return True
        
        print("\nNo se detectó ciclo. La lista es acíclica.")
        return False


# Ejemplo de uso:
lista = ListaEnlazada()


# Agregar nodos a la lista
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)


# Verificar sin ciclo
lista.detectar_ciclo()        # Debería imprimir "No se detectó ciclo"


# Crear un ciclo y verificar
lista.crear_ciclo(1)       # Conecta el último nodo al nodo con valor 2
lista.detectar_ciclo()      # Debería imprimir "¡Ciclo detectado!"
