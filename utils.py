import re

OPERADORES = {"|", ".", "*", "+", "?"}

def tokenizar(expresion): #Convertir una expresión en una lista de tokens
    tokens = []
    i = 0
    expresion = expresion.replace("∗", "*")

    while i < len(expresion):
        if expresion[i].isspace():
            i += 1
            continue

        c = expresion[i]

        if c == "\\":
            if i + 1 < len(expresion):
                tokens.append(expresion[i:i+2])
                i += 2

                continue

        if c == "[":
            j = i

            while j < len(expresion):
                if expresion[j] == "]":
                    break

                j += 1

            tokens.append(expresion[i:j+1])
            i = j + 1

            continue

        if c.isalpha():
            palabra = ""

            while i < len(expresion):
                if expresion[i].isalnum():
                    palabra += expresion[i]
                    i += 1

                else:
                    break

            tokens.append(palabra)

            continue

        tokens.append(c)
        i += 1

    return tokens

def es_operando(token): #Indica si un token es un operando
    if token in {"(", ")"}:
        return False

    if token in OPERADORES:
        return False

    return True

def insertar_concatenacion(tokens): #Inserta el operador de concatenación entre los tokens que lo requieran
    OPERADORES = {"|", "*", "+", "?", "."}


def es_operando(token):
    return (
        token not in OPERADORES
        and token not in {"(", ")"}
    )


def insertar_concatenacion(tokens):
    resultado = []

    for i in range(len(tokens)):
        actual = tokens[i]
        resultado.append(actual)

        if i == len(tokens) - 1:
            continue

        siguiente = tokens[i + 1]

        izquierda = (
            es_operando(actual)
            or actual == ")"
            or actual == "*"
        )

        derecha = (
            es_operando(siguiente)
            or siguiente == "("
        )

        if izquierda and derecha:
            resultado.append(".")

    return resultado

def expandir_question(tokens): #Expande el operador de cero o una ocurrencia
    resultado = []
    i = 0

    while i < len(tokens):
        if tokens[i] != "?":
            resultado.append(tokens[i])
            i += 1
            continue

        operando, inicio = obtener_operando(resultado, len(resultado))
        resultado = resultado[:inicio]

        resultado.extend([
            "(",
            "ε",
            "|"
        ])

        resultado.extend(operando)
        resultado.append(")")

        i += 1

    return resultado

def expandir_plus(tokens): #Expande el operador de una o más ocurrencias
    resultado = []
    i = 0

    while i < len(tokens):
        if tokens[i] != "+":
            resultado.append(tokens[i])

            i += 1
            continue

        operando, inicio = obtener_operando(resultado, len(resultado))

        resultado = resultado[:inicio]

        resultado.extend(operando)
        resultado.append(".")

        resultado.extend(operando)
        resultado.append("*")

        i += 1

    return resultado

def obtener_operando(tokens, indice): #Obtiene el operando a la izquierda de un operador, considerando paréntesis
    fin = indice - 1

    if fin < 0:
        return [], 0

    if tokens[fin] != ")":
        return [tokens[fin]], fin

    contador = 1
    inicio = fin - 1

    while inicio >= 0:
        if tokens[inicio] == ")":
            contador += 1

        elif tokens[inicio] == "(":
            contador -= 1

            if contador == 0:
                break

        inicio -= 1

    return tokens[inicio:fin+1], inicio