def burbuja(lista):
    n = len(lista)
    copia = lista[:]  # Se trabaja con copia para no modificar la original
    total_comparaciones = 0
    total_cambios = 0

    print(f"Lista inicial: {copia}")
    print("\nEjecución del algoritmo:")

    for i in range(n - 1):
        print(f"\n>>> Iteración {i + 1}")
        cambio = False

        for j in range(n - i - 1):
            total_comparaciones += 1
            print(f"Comparando {copia[j]} con {copia[j+1]}")

            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                total_cambios += 1
                cambio = True
                print(f"   Cambio: {copia}")
            else:
                print("   Sin cambio")

        print(f"Estado tras la iteración {i + 1}: {copia}")

        if not cambio:
            print("La lista ya estaba ordenada, se detiene el proceso.")
            break

    print("\nLista ordenada:", copia)
    print("Resumen:")
    print(" Comparaciones realizadas:", total_comparaciones)
    print(" Cambios efectuados:", total_cambios)

    return copia


# Prueba
valores = [64, 34, 25, 12, 22, 11, 90]
print("ORDENAMIENTO BURBUJA")
print("=" * 50)
resultado = burbuja(valores)
