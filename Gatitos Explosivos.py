import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.primero:
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
    
    def eliminar(self, valor):
        actual = self.primero
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.primero:
                    self.primero = actual.siguiente
                if actual == self.ultimo:
                    self.ultimo = actual.anterior
                return
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.cartas = []
    
    def apilar(self, carta):
        self.cartas.append(carta)
    
    def desapilar(self):
        if self.cartas:
            return self.cartas.pop()
        return None
    
    def barajar(self):
        random.shuffle(self.cartas)

class Carta:
    def __init__(self, nombre, accion=None):
        self.nombre = nombre
        self.accion = accion
    
    def ejecutar_accion(self, jugador, juego):
        if self.accion:
            self.accion(jugador, juego)

# Acciones de cartas
def explotar(jugador, juego):
    if "Defuse" in jugador.mano:
        print(f"{jugador.nombre} usó un Defuse y evitó la explosión!")
        jugador.mano.remove("Defuse")
        juego.mazo.apilar(Carta("Exploding Kitten", explotar))  # Regresa la carta al mazo
    else:
        print(f"{jugador.nombre} ha explotado y está fuera del juego!")
        juego.jugadores.remove(jugador)
        juego.turnos.eliminar(jugador)  # Eliminar de la lista de turnos

def barajar_mazo(jugador, juego):
    print(f"{jugador.nombre} ha barajado el mazo.")
    juego.mazo.barajar()

def ver_futuro(jugador, juego):
    print(f"{jugador.nombre} mira las próximas 3 cartas:")
    print([c.nombre for c in juego.mazo.cartas[-3:]])

def atacar(jugador, juego):
    print(f"{jugador.nombre} ha usado Attack. El siguiente jugador toma dos turnos.")
    juego.turnos.agregar(juego.turnos.primero.valor)

def saltar_turno(jugador, juego):
    print(f"{jugador.nombre} ha usado Skip y ha saltado su turno.")
    juego.turnos.eliminar(jugador)

def pedir_favor(jugador, juego):
    if len(juego.jugadores) > 1:
        otro_jugador = random.choice([j for j in juego.jugadores if j != jugador])
        if otro_jugador.mano:
            carta_recibida = random.choice(otro_jugador.mano)
            otro_jugador.mano.remove(carta_recibida)
            jugador.mano.append(carta_recibida)
            print(f"{jugador.nombre} recibió {carta_recibida} de {otro_jugador.nombre}")

def carta_gato(jugador, juego):
    print(f"{jugador.nombre} jugó una carta de gato. Estas cartas no tienen efecto por sí solas.")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
    
    def robar_carta(self, juego):
        carta = juego.mazo.desapilar()
        if carta:
            print(f"{self.nombre} robó la carta {carta.nombre}")
            self.mano.append(carta.nombre)
            carta.ejecutar_accion(self, juego)
            return carta
        return None

class Juego:
    def __init__(self, nombres_jugadores):
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.mazo = Pila()
        self.turnos = ListaDoblementeEnlazada()
    
    def iniciar_juego(self):
        for jugador in self.jugadores:
            self.turnos.agregar(jugador)
            jugador.mano.append("Defuse")
        
        # Agregar explosiones según la cantidad de jugadores
        for _ in range(len(self.jugadores) - 1):
            self.mazo.apilar(Carta("Exploding Kitten", explotar))

        # Agregar otras cartas
        cartas_disponibles = [
            Carta("Defuse"), Carta("Attack", atacar), Carta("Skip", saltar_turno),
            Carta("Favor", pedir_favor), Carta("Shuffle", barajar_mazo),
            Carta("See the Future", ver_futuro),
            Carta("Tacocat", carta_gato), Carta("Hairy Potato Cat", carta_gato),
            Carta("Rainbow Ralphing Cat", carta_gato), Carta("Cattermelon", carta_gato),
            Carta("Beard Cat", carta_gato)
        ]
        
        for carta in cartas_disponibles:
            self.mazo.apilar(carta)
        
        self.mazo.barajar()
    
    def jugar(self):
        while len(self.jugadores) > 1:
            jugador = self.turnos.primero.valor
            print(f"Es el turno de {jugador.nombre}")
            
            input("Presiona ENTER para robar una carta...")  # Pausar para interacción
            
            carta = jugador.robar_carta(self)

            if jugador not in self.jugadores:  # Si el jugador explotó, no lo reingresamos
                continue

            # Si quedan solo 2 jugadores, forzamos a que el juego termine
            if len(self.jugadores) == 2:
                print(f"⚠️ Solo quedan {self.jugadores[0].nombre} y {self.jugadores[1].nombre}. ¡El juego debe terminar pronto!")
                continue  # No volvemos a agregar el turno, seguimos jugando hasta que explote uno
            
            self.turnos.eliminar(jugador)  # Quitar del turno actual
            self.turnos.agregar(jugador)  # Reagregar al final si sigue en el juego

        print(f"🎉 {self.jugadores[0].nombre} es el ganador!")  # Un jugador queda y gana

# Ejemplo de uso con 5 jugadores
juego = Juego(["Alice", "Bob", "Charlie", "David", "Eve"])
juego.iniciar_juego()
juego.jugar()
