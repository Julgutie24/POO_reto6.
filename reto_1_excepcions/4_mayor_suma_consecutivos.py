
def mayor_suma_consecutivos(lista):
    try:
        if len(lista) < 2:
            raise ValueError("La lista debe tener al menos dos elementos.")
        for n in lista:
            if not isinstance(n, (int, float)):
                raise TypeError("Todos los elementos deben ser números.")

        max_suma = lista[0] + lista[1]
        for i in range(1, len(lista) - 1):
            suma = lista[i] + lista[i + 1]
            if suma > max_suma:
                max_suma = suma
        return max_suma
    except Exception as e:
        return f"Error: {e}"

print(mayor_suma_consecutivos([5]))  # ValueError: no hay suficientes elementos
print(mayor_suma_consecutivos([1, 'a', 3]))  # TypeError: 'a' no es número