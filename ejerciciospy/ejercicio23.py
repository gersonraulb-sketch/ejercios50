# divide el texto por espacios y cuenta las palabras

def contar_palabras(texto):
    return len(texto.split())

# cuenta caracteres


def contar_caracteres(texto, incluir_espacios=True):
    if incluir_espacios:
        return len(texto)
    else:
        return len(texto.replace(" ", ""))

# encuentra la palabra más larga


def palabra_mas_larga(texto):
    palabras = texto.split()
    return max(palabras, key=len)

# verifica si el texto es un palíndromo


def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]


frase = input("Escribe un texto: ")

print("\n--- ANALIZADOR DE TEXTO ---")
print(f"Texto: {frase}")
print(f"Cantidad de palabras: {contar_palabras(frase)}")
print(f"Caracteres (con espacios): {contar_caracteres(frase)}")
print(f"Caracteres (sin espacios): {contar_caracteres(frase, False)}")
print(f"Palabra más larga: {palabra_mas_larga(frase)}")
print(f"¿Es palíndromo?: {es_palindromo(frase)}")
