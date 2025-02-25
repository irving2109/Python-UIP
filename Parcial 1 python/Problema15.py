from collections import deque

class SistemaPedidos:
    def __init__(self, num_repartidores):
        self.pedidos_urgentes = deque()          # Cola para pedidos urgentes
        self.pedidos_normales = deque()         # Cola para pedidos normales
        self.repartidores_disponibles = list(range(1, num_repartidores + 1))        # Lista de repartidores disponibles
        self.repartidores_ocupados = {}         # Diccionario para pedidos en curso {repartidor: pedido}

    # Agregar un pedido a la cola correspondiente
    def agregar_pedido(self, tipo, descripcion):
        if tipo == "urgente":
            self.pedidos_urgentes.appendleft(descripcion)         # Se agrega al frente de la cola urgente
            print(f"\nPedido URGENTE agregado: {descripcion}")
        elif tipo == "normal":
            self.pedidos_normales.append(descripcion)               # Se agrega al final de la cola normal
            print(f"\nPedido NORMAL agregado: {descripcion}")
        else:
            print("\nTipo de pedido no válido. Debe ser 'urgente' o 'normal'.")



    # Asignar pedidos a repartidores disponibles
    def asignar_pedidos(self):
        print("\nAsignando pedidos...")
        while self.repartidores_disponibles:
            # Priorizar pedidos urgentes
            if self.pedidos_urgentes:
                pedido = self.pedidos_urgentes.pop()
                repartidor = self.repartidores_disponibles.pop(0)
                self.repartidores_ocupados[repartidor] = pedido
                print(f"Repartidor {repartidor} asignado a pedido URGENTE: {pedido}")
            # Luego atender pedidos normales
            elif self.pedidos_normales:
                pedido = self.pedidos_normales.popleft()
                repartidor = self.repartidores_disponibles.pop(0)
                self.repartidores_ocupados[repartidor] = pedido
                print(f"Repartidor {repartidor} asignado a pedido NORMAL: {pedido}")
            else:
                print("No hay más pedidos pendientes.")
                break



    # Mostrar todos los pedidos pendientes
    def mostrar_pedidos_pendientes(self):
        print("\nPedidos URGENTES pendientes:", list(self.pedidos_urgentes))
        print("Pedidos NORMALES pendientes:", list(self.pedidos_normales))



    # Finalizar entrega y liberar repartidor
    def finalizar_entrega(self, repartidor):
        if repartidor in self.repartidores_ocupados:
            pedido_entregado = self.repartidores_ocupados.pop(repartidor)
            self.repartidores_disponibles.append(repartidor)
            print(f"\nRepartidor {repartidor} ha entregado el pedido: {pedido_entregado}")
        else:
            print(f"\nEl repartidor {repartidor} no está asignado a ningún pedido.")

# Ejemplo de su uso:
sistema = SistemaPedidos(num_repartidores=3)


# Agregar pedidos
sistema.agregar_pedido("normal", "Pedido 1 - Cliente A")
sistema.agregar_pedido("urgente", "Pedido 2 - Cliente B (Urgente)")
sistema.agregar_pedido("normal", "Pedido 3 - Cliente C")
sistema.agregar_pedido("urgente", "Pedido 4 - Cliente D (Urgente)")
sistema.agregar_pedido("normal", "Pedido 5 - Cliente E")


# Mostrar pedidos pendientes
sistema.mostrar_pedidos_pendientes()


# Asignar pedidos a repartidores
sistema.asignar_pedidos()


# Finalizar entregas
sistema.finalizar_entrega(1)
sistema.finalizar_entrega(2)


# Mostrar pedidos pendientes después de asignación
sistema.mostrar_pedidos_pendientes()


# Asignar pedidos nuevamente (repartidores libres)
sistema.asignar_pedidos()
