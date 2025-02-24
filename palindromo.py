def main():
    palabra = input("Ingresa una palabra: ")
    
    # Guardar en una lista (simulando una pila y una cola)
    mi_lista = [letra for letra in palabra]
    
    # Verificar si es palíndromo
    if mi_lista == mi_lista[::-1]:
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")

if __name__ == "__main__":
    main()
    