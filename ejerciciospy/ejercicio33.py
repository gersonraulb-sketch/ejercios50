import random
import time


def crear_tablero(filas, columnas, densidad=0.3):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero


def contar_vecinos_vivos(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos


def aplicar_reglas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    cambios = []
    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]
            nueva_celula = celula_actual
            if celula_actual == 1:
                if vecinos < 2:
                    nueva_celula = 0
                    cambios.append((i, j, "murió por soledad"))
                elif vecinos > 3:
                    nueva_celula = 0
                    cambios.append((i, j, "murió por sobrepoblación"))
            else:
                if vecinos == 3:
                    nueva_celula = 1
                    cambios.append((i, j, "nació"))
            nuevo_tablero[i][j] = nueva_celula
    return nuevo_tablero, cambios


def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
    print(f"\nGeneración {generacion}")
    for i, fila in enumerate(tablero):
        linea = ""
        for j, celula in enumerate(fila):
            if celula == 1:
                linea += "⬛"
            else:
                linea += "⬜"
        if mostrar_coordenadas:
            linea += f"  <- fila {i}"
        print(linea)


if __name__ == "__main__":
    filas, columnas = 15, 30
    tablero = crear_tablero(filas, columnas, densidad=0.3)
    generaciones = 20

    for gen in range(1, generaciones + 1):
        mostrar_tablero(tablero, gen)
        tablero, cambios = aplicar_reglas(tablero)
        print(f"Cambios en esta generación: {len(cambios)}")
        time.sleep(0.3)
