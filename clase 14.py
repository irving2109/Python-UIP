grafo = {
'A': ['B','C'],
'B': ['A', 'C', 'D'],
'C': ['A', 'B', 'D'],
'D': ['B', 'C', 'E'],
'E': ['D'],

}

# imprimir grado de cada nodo
def imprimir_grafo(grafo):
    print("Grado de cada vertice:")
    for nodo in grafo:
        grado = len(grafo[nodo])
        print(f"{nodo}:{grado}")


def vertice_mayor_grado(grafo):
    max_nodo = None
    max_grado  = -1
    for nodo in grafo:
        grado = len (grafo[nodo])
        if grado > max_grado:
            max_grado = grado
            max_nodo = nodo
    return max_grado, max_nodo

def es_regular (grafo):
    grados = [len(grafo[nodo])for nodo in grafo]
    return all (grado == grados [0] for grado in grados)

#ejecutar funcion
imprimir_grafo (grafo)

nodo_max, grado_max = vertice_mayor_grado(grafo)
print(f"nodo con mayor grado: {nodo_max} (grado {grado_max})")

if es_regular (grafo):
    print ("el grafo es regular(todos los nodos tienen el mismo grado)")
else:
    print ("el grafo no es regular")

