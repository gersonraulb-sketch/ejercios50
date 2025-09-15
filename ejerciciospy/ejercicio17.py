# Lista de compras inteligente
compras = ["arroz", "pollo", "tomates"]
print("Lista inicial:")
print(compras)
# Agregar más compras
compras.extend(["aceite", "huevos"])  # extend() agrega múltiples elementos
print("\nDespués de agregar aceite y huevos:")
print(compras)
# Insertar en posición específica
compras.insert(1, "mantequilla")  # insert(posición, elemento)
print("\nDespués de insertar mantequilla en posición 1:")
print(compras)
# Eliminar elementos
compras.remove("arroz")  # remove(elemento)
print("\nDespués de eliminar arroz:")
print(compras)
# Eliminar por posición
elemento_eliminado = compras.pop(3)
print("\nEliminamos el primer elemento:", elemento_eliminado)
print("Lista final:", compras)
