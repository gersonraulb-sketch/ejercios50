from collections import Counter
import heapq


class NodoHuffman:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def comprimir_repeticion_simple(texto):
    if not texto:
        return ""
    resultado = []
    contador = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            resultado.append(f"{contador}{texto[i - 1]}")
            contador = 1
    resultado.append(f"{contador}{texto[-1]}")
    return "".join(resultado)


def construir_arbol_huffman(texto):
    frecuencia = Counter(texto)
    heap = [NodoHuffman(char, freq) for char, freq in frecuencia.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        nuevo_nodo = NodoHuffman(None, izq.freq + der.freq, izq, der)
        heapq.heappush(heap, nuevo_nodo)

    return heap[0]  # raíz


def generar_codigos(nodo, codigo="", diccionario=None):
    if diccionario is None:
        diccionario = {}
    if nodo.char is not None:  # hoja
        diccionario[nodo.char] = codigo
    else:
        generar_codigos(nodo.left, codigo + "0", diccionario)
        generar_codigos(nodo.right, codigo + "1", diccionario)
    return diccionario


def comprimir_huffman(texto):
    if not texto:
        return "", {}

    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos(arbol)
    texto_codificado = "".join(codigos[char] for char in texto)
    return texto_codificado, codigos


if __name__ == "__main__":
    texto = "aaabbcddddeeaaaa"

    print("Texto original:", texto)
    print("Tamaño original:", len(texto))

    rle = comprimir_repeticion_simple(texto)
    print("\nCompresión por repeticiones (RLE):", rle)
    print("Tamaño comprimido:", len(rle))

    huffman_codificado, codigos = comprimir_huffman(texto)
    print("\nCompresión Huffman (binario):", huffman_codificado)
    print("Diccionario de códigos:", codigos)
    print("Tamaño comprimido (bits):", len(huffman_codificado))
