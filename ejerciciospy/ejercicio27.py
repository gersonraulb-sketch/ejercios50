def busqueda_binaria(lista, x):
    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2
        if lista[medio] == x:
            print(f"Binaria encontró {x} en {medio} en {pasos} pasos")
            return medio
        elif lista[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1

    print(f"Binaria no encontró {x} en {pasos} pasos")
    return -1


def busqueda_lineal(lista, x):
    for i, valor in enumerate(lista, start=1):
        if valor == x:
            print(f"Lineal encontró {x} en {i-1} en {i} pasos")
            return i - 1
    print(f"Lineal no encontró {x} en {len(lista)} pasos")
    return -1


# Prueba
numeros = [11, 22, 25, 34, 44, 55, 66, 77, 88, 99]
buscar = 55

print("Lista:", numeros)
print("Buscando:", buscar)

busqueda_binaria(numeros, buscar)
busqueda_lineal(numeros, buscar)
