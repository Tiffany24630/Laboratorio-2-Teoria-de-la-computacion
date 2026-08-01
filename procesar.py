from utils import tokenizar, expandir_plus, expandir_question, insertar_concatenacion
from shunting_yard import shunting_yard

def procesar(expresion): #Procesa una expresión regular y la convierte a notación postfix
    print("=" * 70)
    print("Expresión original:")
    print(expresion)

    tokens = tokenizar(expresion)

    print("\nTokens:")
    print(tokens)

    tokens = expandir_plus(tokens)

    print("\nDespués de expandir +:")
    print(tokens)

    tokens = expandir_question(tokens)

    print("\nDespués de expandir ?:")
    print(tokens)

    tokens = insertar_concatenacion(tokens)

    print("\nDespués de insertar concatenación:")
    print(tokens)

    postfix = shunting_yard(tokens)

    print("\nPostfix:")
    print(" ".join(postfix))