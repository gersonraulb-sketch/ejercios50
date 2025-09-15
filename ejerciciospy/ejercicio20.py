import random
valores = [15, 3, 99, 42, 8, 73, 27, 64, 5, 50]

print("Lista original:", valores)
print("Cantidad de elementos:", len(valores))

# Crear copias para no modificar la original
asc = valores.copy()
desc = valores.copy()
mezcla = valores.copy()
inversa = valores.copy()

# Ordenar de menor a mayor (usando sorted)
asc = sorted(valores)
print("\nOrdenada ascendente:", asc)

# Ordenar de mayor a menor (también con sorted)
desc = sorted(valores, reverse=True)
print("Ordenada descendente:", desc)

# Mezclar la lista
random.shuffle(mezcla)
print("Lista mezclada:", mezcla)

# Invertir el orden actual
inversa.reverse()
print("Orden invertido:", inversa)

# Extras: obtener máximo y mínimo
print(f"Valor máximo: {max(valores)}")
print(f"Valor mínimo: {min(valores)}")

print("\nLista original (sin cambios):", valores)
