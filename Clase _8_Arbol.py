class Nodo:
    def _init_(self, clave):
        self.izquierda = None
        self.derecha = None
        self.clave = clave
        
class ArbolBinario:
    def _init_(self):
        self.raiz = None
        
    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar_recursivo(self.raiz, clave)
        
    def _insertar_recursivo(self, nodo, clave):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave)
            else:
                self._insertar_recursivo(nodo.izquierda, clave)

        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave)
            else:
                self._insertar_recursivo(nodo.derecha, clave)
                
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.clave, end=" ")
            self.recorrido_inorden(nodo.derecha)
            
    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.clave, end=" ")
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)
            
    def recorrido_posorden(self, nodo):
        if nodo:
            self.recorrido_posorden(nodo.izquierda)
            self.recorrido_posorden(nodo.derecha)
            print(nodo.clave, end=" ")
        
        
#llamar al arbol
arbol = ArbolBinario()
valores = [5, 3, 1, 8, 4]

for i in valores:
    arbol.insertar(i)
    
print("Recorrido inorden")
arbol.recorrido_inorden(arbol.raiz)
print("\nRecorrido preorden")
arbol.recorrido_preorden(arbol.raiz)
print("\nRecorrido postorden")
arbol.recorrido_posorden(arbol.raiz)