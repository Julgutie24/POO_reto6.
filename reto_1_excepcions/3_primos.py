
def es_primo(n):
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero.")
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    try:
        return [n for n in lista if es_primo(n)]
    except TypeError as e:
        return f"Error: {e}"

print(filtrar_primos([2, 3, "5", 7]))  # TypeError: "5" es string