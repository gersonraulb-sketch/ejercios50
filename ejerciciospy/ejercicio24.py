import random
import string


def generar_contraseña(longitud=8, mayus=True, numeros=True, simbolos=False):
    caracteres = string.ascii_lowercase

    if mayus:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%&*"

    # Construir la contraseña
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña


def evaluar_fortaleza(contraseña):
    puntos = 0
    detalles = []

    # Longitud mínima 8
    if len(contraseña) >= 8:
        puntos += 2
        detalles.append("Longitud adecuada")
    else:
        detalles.append("Muy corta (mínimo 8)")

    # Tiene mayúsculas
    if any(c.isupper() for c in contraseña):
        puntos += 1
        detalles.append("Contiene mayúsculas")
    else:
        detalles.append("Sin mayúsculas")

    # Tiene números
    if any(c.isdigit() for c in contraseña):
        puntos += 1
        detalles.append("Contiene números")
    else:
        detalles.append("Sin números")

    # Clasificación final
    if puntos >= 4:
        nivel_fortaleza = "Muy fuerte"
    elif puntos == 3:
        nivel_fortaleza = "Fuerte"
    elif puntos == 2:
        nivel_fortaleza = "Moderada"
    else:
        nivel_fortaleza = "Débil"

    return nivel_fortaleza, detalles


# --- Programa principal ---
print("GENERADOR DE CONTRASEÑAS")
print("=" * 35)

# Ejemplos
contraseñas = [
    ("Estándar (12 caracteres)", generar_contraseña(12, True, False, False)),
    ("Con símbolos (10 caracteres)", generar_contraseña(10, True, True, True)),
    ("Solo minúsculas (6 caracteres)", generar_contraseña(6, False, False, False))
]

# Mostrar resultados
for desc, pwd in contraseñas:
    fortaleza, detalles = evaluar_fortaleza(pwd)
    print(f"\n{desc}:")
    print(f"Contraseña: {pwd}")
    print(f"Fortaleza: {fortaleza}")
    for c in detalles:
        print("  -", c)
