
def mismos_caracteres(lista):
    try:
        for s in lista:
            if not isinstance(s, str):
                raise TypeError("Todos los elementos deben ser cadenas de texto.")

        resultado = []
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if sorted(lista[i]) == sorted(lista[j]):
                    if lista[i] not in resultado:
                        resultado.append(lista[i])
                    if lista[j] not in resultado:
                        resultado.append(lista[j])
        return resultado
    except Exception as e:
        return f"Error: {e}"

print(mismos_caracteres(["amor", "roma", 123]))  # TypeError: 123 no es string