from collections import deque

def es_palindromo(palabra_palindromo):
    palabra_palindromo = palabra_palindromo.lower().replace(" ", "")

    pila = []
    cola = deque()

    for letra in palabra_palindromo:
        pila.append(letra)
        cola.append(letra)

    while pila:
        if pila.pop() != cola.popleft():
            return False

    return True
palabra_palindromo = input("Ingrese una palabra para que registre el usuario y que contenga las ultimas letras iguales: ")

if es_palindromo(palabra_palindromo):
    print(f"{palabra_palindromo} la palabra es correcta es un palindromo.")
else:
    print(f"{palabra_palindromo}  error la palabra no es un palindromo.")