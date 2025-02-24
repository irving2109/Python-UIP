def main():
    palabra = input("Ingresa una palabra: ")
    
    # Guardar en una pila (LIFO)
    pila = []
    for letra in palabra:
        pila.append(letra)
    
    print("Pila (LIFO):", pila)
    
    # Transferir a una cola (FIFO)
    cola = []
    for letra in pila:
        cola.append(letra)
    
    print("Cola (FIFO):", cola)
    
    # Verificar si es palíndromo
    if palabra == palabra[::-1]:
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")

if __name__ == "__main__":
    main()
