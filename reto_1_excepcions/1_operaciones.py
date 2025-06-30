class OperacionInvalida(Exception):

    pass

def calcular(a, b, operacion):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos operandos deben ser numéricos.")

        if operacion == '+':
            return a + b
        elif operacion == '-':
            return a - b
        elif operacion == '*':
            return a * b
        elif operacion == '/':
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return a / b
        else:
            raise OperacionInvalida("Operación no válida.")
    except TypeError as e:
        return f"Error: {e}"
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except OperacionInvalida as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(calcular(5, 0, '/'))     # Error: No se puede dividir por cero.
    print(calcular(5, 'a', '*'))   # Error: Ambos operandos deben ser numéricos.
    print(calcular(5, 2, '%'))     # Error: Operación no válida.
    print(calcular(5, 3, '+'))     #todo melo
    print(calcular(4.5, 1.5, '*')) #todo melo