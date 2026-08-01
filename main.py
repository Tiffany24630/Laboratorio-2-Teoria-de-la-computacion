from procesar import procesar 

with open("expresiones.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                procesar(linea)