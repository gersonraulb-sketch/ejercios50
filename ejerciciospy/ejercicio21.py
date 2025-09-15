def saludar(nombre):
    return f"¡Hola {nombre}! ¿Cómo estás?"


# Pedir los nombres
nombres = []
for i in range(3):
    nombre_ingresado = input(f"Escribe el nombre {i+1}: ")
    nombres.append(nombre_ingresado)

# Saludar a cada uno
for n in nombres:
    print(saludar(n))
