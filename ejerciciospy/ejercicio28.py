def contar_frecuencias(lista):  # Cuenta la frecuencia de cada elemento en la lista
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias


def mostrar_estadisticas(frecuencias):  # Muestra estadísticas de frecuencia
    print("\nESTADÍSTICAS DE FRECUENCIA")
    print("-" * 40)

    total = sum(frecuencias.values())
    print(f"Total de elementos: {total}")
    print(f"Elementos únicos: {len(frecuencias)}\n")

    # Ordenar por frecuencia (mayor a menor)
    ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    for elem, freq in ordenados:
        porcentaje = (freq / total) * 100
        print(f"{elem}: {freq} veces ({porcentaje:.1f}%)")

    # Más frecuente
    mas_comun = max(frecuencias, key=frecuencias.get)
    print(
        f"\nElemento más frecuente: {mas_comun} ({frecuencias[mas_comun]} veces)")


numeros = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]
print("Lista de números:", numeros)
frecuencias_numeros = contar_frecuencias(numeros)
mostrar_estadisticas(frecuencias_numeros)


palabra = "programacion"
letras = list(palabra)
print("\nPalabra:", palabra)
frecuencias_letras = contar_frecuencias(letras)
mostrar_estadisticas(frecuencias_letras)
