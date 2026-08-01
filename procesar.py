from utils import tokenizar, expandir_plus, expandir_question, insertar_concatenacion
from shunting_yard import shunting_yard
from balanceador import balanceada

def procesar(expresion): #Procesa una expresión regular y la convierte a notación postfix
    print("=" * 70)
    print("Expresión original:")
    print(expresion)

    if not balanceada(expresion):
        print("\nERROR: expresión no balanceada.")
        return

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

    try:
        postfix = shunting_yard(tokens)

    except ValueError as e:
        print("\nERROR:", e)
        return

    print("\nPostfix:")
    print(" ".join(postfix))