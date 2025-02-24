from collections import deque

def esta_balanceado(expresion):
    # Diccionario de pares de apertura y cierre
    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Usamos deque como pila
    pila = deque()

    # Recorrer cada carácter de la expresión
    for char in expresion:
        # Si es un paréntesis/corchete/llave de apertura, lo empujamos a la pila
        if char in '({[':
            pila.append(char)
        # Si es un paréntesis/corchete/llave de cierre
        elif char in ')}]':
            # Verificamos si la pila está vacía o si el tope no coincide con el cierre actual
            if not pila or pila.pop() != pares[char]:
                return False

    # Si la pila está vacía al final, está balanceado
    return not pila

# Ejemplos de uso:
expresiones = [
    "({[()]})",
    "({[(])})",
    "{[()]}",
    "((()))",
    "({[})]"
]

for exp in expresiones:
    if esta_balanceado(exp):
        print(f"{exp} → Balanceado ✅")
    else:
        print(f"{exp} → No balanceado ❌")
