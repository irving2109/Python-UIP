class Estudiante:
    def __init__(self, nombre, matricula, calificacion):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion = calificacion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, matricula, calificacion):
        nuevo_estudiante = Estudiante(nombre, matricula, calificacion)
        nuevo_estudiante.siguiente = self.cabeza
        self.cabeza = nuevo_estudiante

    def mostrar_estudiantes(self):
        nodo_actual = self.cabeza
        print("\nListado de estudiantes:")
        while nodo_actual:
            print(f"Nombre: {nodo_actual.nombre}, Matrícula: {nodo_actual.matricula}, Calificación: {nodo_actual.calificacion}")
            nodo_actual = nodo_actual.siguiente

    def mejor_calificacion(self):
        nodo_actual = self.cabeza
        mejor_estudiante = None
        mejor_calificacion = float('-inf')

        while nodo_actual:
            if nodo_actual.calificacion > mejor_calificacion:
                mejor_calificacion = nodo_actual.calificacion
                mejor_estudiante = nodo_actual.nombre
            nodo_actual = nodo_actual.siguiente

        return mejor_estudiante

# Ejemplo de uso:
estudiantes = ListaEnlazada()
estudiantes.agregar('Juan', 'A001', 85)
estudiantes.agregar('Ana', 'A002', 92)
estudiantes.agregar('Luis', 'A003', 88)
estudiantes.agregar('Marta', 'A004', 95)

# Mostrar todos los estudiantes
estudiantes.mostrar_estudiantes()

# Mostrar el estudiante con la mejor calificación
print("\nEl estudiante con la mejor calificación es:", estudiantes.mejor_calificacion())