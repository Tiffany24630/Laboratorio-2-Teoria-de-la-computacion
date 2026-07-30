from balanceador import Balanceador

balanceador = Balanceador()
archivo = "expresions.txt"

with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        expresion = linea.strip()

        if expresion == "":
            continue

        balanceador.verificar(expresion)