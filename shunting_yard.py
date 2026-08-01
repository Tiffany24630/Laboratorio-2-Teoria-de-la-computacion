from stack import Stack

PRIORIDAD = {
    "|": 1,
    ".": 2,
    "*": 3
}

def shunting_yard(tokens):
    salida = []
    pila = Stack()

    print("\nProceso:\n")

    for token in tokens:
        print("--------------------------------")
        print("Token:", token)

        if token not in PRIORIDAD and token not in {"(", ")"}:
            salida.append(token)

        elif token == "(":
            pila.push(token)

        elif token == ")":
            while not pila.is_empty() and pila.peek() != "(":
                salida.append(pila.pop())

            pila.pop()

        else:
            while (
                not pila.is_empty()
                and pila.peek() != "("
                and PRIORIDAD.get(pila.peek(), 0)
                >= PRIORIDAD[token]
            ):
                salida.append(pila.pop())

            pila.push(token)

        print("Pila :", pila)
        print("Salida:", salida)

    while not pila.is_empty():
        salida.append(pila.pop())

    return salida