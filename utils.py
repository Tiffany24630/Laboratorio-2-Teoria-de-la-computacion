import re

def tokenizar(expresion): #Convertir una expresión en una lista de tokens
    tokens = []
    i = 0

    while i < len(expresion):
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

