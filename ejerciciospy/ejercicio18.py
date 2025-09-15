# Calculadora de calificaciones
calificaciones = []
while len(calificaciones) < 6:
    nota = float(input("Ingrese sus calificaciones (0-20): "))
    if 0 <= nota <= 20:
        calificaciones.append(nota)  # Agredar nota a la lista
    else:
        print("Nota inválida")

print("Notas del estudiante:")
print(calificaciones)

# Estadísticas básicas
total_mat = len(calificaciones)       # cuántas notas hay
sum_notas = sum(calificaciones)       # suma todas las notas
promedio = sum_notas / total_mat      # promedio general
nota_max = max(calificaciones)        # nota más alta
nota_min = min(calificaciones)        # nota más baja

# Mostrar resultados
print("\n      ESTADÍSTICAS     ")
print(f"Total de materias: {total_mat}")
print(f"Suma de todas las notas: {sum_notas}")
print(f"Promedio: {promedio:.2f}")  # :.2f redondea a 2 decimales
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")
# Contar notas aprobadas (>=7.0)
aprobadas = 0
for nota in calificaciones:  # for recorre cada elemento
    if nota >= 7.0:
        aprobadas = aprobadas + 1
print(f"Materias aprobadas: {aprobadas} de {total_mat}")
