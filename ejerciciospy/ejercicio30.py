def calcular_similitud(usuario1, usuario2):
    """
    Calcula similitud entre dos usuarios basada en gustos comunes
    Retorna un valor entre 0 (muy diferentes) y 1 (muy similares)
    """
    gustos_comunes = 0
    total_comparaciones = 0

    for categoria in usuario1:
        if categoria in usuario2:
            total_comparaciones += 1
            if usuario1[categoria] == usuario2[categoria]:
                gustos_comunes += 1

    if total_comparaciones == 0:
        return 0

    return round(gustos_comunes / total_comparaciones, 2)


def encontrar_usuarios_similares(usuario_obj, base_usuarios, umbral=0.6):
    """Encuentra usuarios similares al usuario objetivo"""
    similares = []
    gustos_objetivo = base_usuarios[usuario_obj]

    print(
        f"Buscando usuarios similares a '{usuario_obj}' (umbral: {umbral})")
    print("-" * 40)

    for nombre_usuario, gustos_usuario in base_usuarios.items():
        if nombre_usuario != usuario_obj:
            similitud = calcular_similitud(gustos_objetivo, gustos_usuario)
            print(f"{nombre_usuario}: similitud = {similitud}")
            if similitud >= umbral:
                similares.append((nombre_usuario, similitud))

    similares.sort(key=lambda x: x[1], reverse=True)
    return similares


def recomendar_contenido(usuario_obj, usuarios_similares, base_usuarios):
    """Recomienda contenido basado en usuarios similares"""
    gustos_objetivo = base_usuarios[usuario_obj]
    recomendaciones = {}

    print(f"\nGenerando recomendaciones para '{usuario_obj}':")
    for nombre_similar, similitud in usuarios_similares:
        gustos_similar = base_usuarios[nombre_similar]
        print(
            f"\nAnalizando gustos de {nombre_similar} (similitud: {similitud}):")

        for categoria, le_gusta in gustos_similar.items():
            if categoria not in gustos_objetivo and le_gusta:
                if categoria not in recomendaciones:
                    recomendaciones[categoria] = []
                recomendaciones[categoria].append((nombre_similar, similitud))
                print(
                    f" → Recomendar '{categoria}' (le gusta a {nombre_similar})")

    return recomendaciones


# Base de datos de usuarios y sus gustos
usuarios = {
    "Ana": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": True},
    "Carlos": {"acción": True, "comedia": False, "drama": True, "terror": False, "ciencia_ficción": True},
    "María": {"acción": False, "comedia": True, "drama": True, "terror": True, "ciencia_ficción": False},
    "Pedro": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": False},
    "Laura": {"acción": False, "comedia": True, "drama": True, "terror": False, "ciencia_ficción": True}
}

print("SISTEMA DE RECOMENDACIONES")
print("=" * 35)
print("Base de usuarios:")
for usuario, gustos in usuarios.items():
    print(f"{usuario}: {gustos}")

print("\n" + "=" * 50)

# Buscar similares para Ana
usuario_obj = "Ana"
similares = encontrar_usuarios_similares(usuario_obj, usuarios, 0.4)

print(f"\nUsuarios similares a {usuario_obj}:")
for similar, similitud in similares:
    print(f" {similar}: {similitud * 100:.0f}% similar")

# Generar recomendaciones
recomendaciones = recomendar_contenido(usuario_obj, similares, usuarios)

print("\n" + "=" * 30)
print("RECOMENDACIONES FINALES")
print("=" * 30)
if recomendaciones:
    for categoria, recomendadores in recomendaciones.items():
        fuentes = ", ".join([f"{u} ({s*100:.0f}%)" for u, s in recomendadores])
        print(f"{categoria}: recomendado por {fuentes}")
else:
    print("No hay recomendaciones disponibles.")
