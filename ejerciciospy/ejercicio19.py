# Lista de frutas
frutas = ["manzana", "banana", "uva", "kiwi", "pera", "mango", "banana"]
print("Lista de frutas:", frutas)

fruta_buscada = input(
    "¿qué animales desea buscar? (si es más de uno usa ,) ").replace(" ", "").split(",")

for fruta in fruta_buscada:
    if fruta in frutas:
        print(f"La fruta '{fruta}' se encuentra en la lista.")

        print(f"La posición de {fruta} es: {frutas.index(fruta)}")

        print(f"Y aparece {frutas.count(fruta)} veces.")
    else:
        print(f"La fruta '{fruta}' no esta en la lista.")
