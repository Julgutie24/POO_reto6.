
def es_palindromo(palabra):
    try:
        if not isinstance(palabra, str):
            raise TypeError("El argumento debe ser una cadena de texto.")

        longitud = len(palabra)
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - 1 - i]:
                return False
        return True
    except TypeError as e:
        return f"Error: {e}"

print(es_palindromo(12321))  # TypeError: se esperaba una cadena