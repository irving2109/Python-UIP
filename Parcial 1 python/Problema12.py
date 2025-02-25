from collections import deque

class FilaClientes:
    def __init__(self):
        self.fila = deque()

    # llegada_cliente(nombre): Agregar un cliente al final de la fila
    def llegada_cliente(self, nombre):
        self.fila.append(nombre)
        print(f"\n{nombre} ha llegado y está en la fila.")

    # atender_cliente(): Atender al cliente en la parte frontal de la fila
    def atender_cliente(self):
        if self.esta_vacia():
            print("\nNo hay clientes en la fila.")
            return None
        cliente = self.fila.popleft()
        print(f"\nSe está atendiendo a {cliente}.")
        return cliente

    # mostrar_fila(): Mostrar todos los clientes en la fila
    def mostrar_fila(self):
        print("\nFila de clientes:")
        if self.esta_vacia():
            print("No hay clientes en la fila.")
        else:
            for cliente in self.fila:
                print(cliente, end=" -> ")
            print("None")

    # Verificar si la fila está vacía
    def esta_vacia(self):
        return len(self.fila) == 0

# Ejemplo de uso:
fila = FilaClientes()

# Llegan clientes a la fila
fila.llegada_cliente("Juan")
fila.llegada_cliente("Ana")
fila.llegada_cliente("Luis")

# Mostrar fila de clientes
fila.mostrar_fila()

# Atender a los clientes
fila.atender_cliente()
fila.mostrar_fila()

fila.atender_cliente()
fila.atender_cliente()
fila.atender_cliente()  # Intento de atender cuando no hay clientes
