from stack import Stack

class Balanceador:
    def __init__(self):
        self.apertura = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        self.cierre = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

    def verificar(self, expresion):
        pila = Stack()

        print("\nExpresión:", expresion)

        for i, caracter in enumerate(expresion):
            if caracter in self.apertura:
                pila.push(caracter)

                print(f"'{caracter}' PUSH\tPila = {pila}")

            elif caracter in self.cierre:
                if pila.is_empty():
                    print(f"'{caracter}' ERROR " "(la pila está vacía)")

                    return False

                ultimo = pila.pop()

                print(f"'{caracter}' POP '{ultimo}'\tPila = {pila}")

                if ultimo != self.cierre[caracter]:
                    print("No coincide el símbolo de apertura.")
                    return False

        if pila.is_empty():
            print("Resultado: Expresión balanceada")
            return True

        else:
            print("Resultado: Quedaron símbolos sin cerrar, no se pudo balancear la expresión", pila)
            return False