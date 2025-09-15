# Lista donde guardamos los datos
estudiantes = []


def agregar_estudiante(nombre, edad, grado):  # Agrega un nuevo estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado,
        "calificaciones": []
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado")


def buscar_estudiante(nombre):  # Busca un estudiante por nombre
    for i, estudiante in enumerate(estudiantes):
        if estudiante["nombre"].lower() == nombre.lower():
            return i
    return -1


def registrar_nota(nombre, materia, nota):  # Agrega una calificación a un estudiante
    pos = buscar_estudiante(nombre)
    if pos != -1:
        estudiantes[pos]["calificaciones"].append(
            {"materia": materia, "nota": nota})
        print(f"Nota agregada a {nombre}: {materia} = {nota}")
    else:
        print(f"Estudiante {nombre} no existe")


def calcular_promedio(nombre):  # Calcula el promedio de un estudiante
    pos = buscar_estudiante(nombre)
    if pos != -1:
        notas = [c["nota"] for c in estudiantes[pos]["calificaciones"]]
        if notas:
            return round(sum(notas) / len(notas), 2)
        else:
            return 0
    return None


def mostrar_reporte():  # Muestra el reporte de todos los estudiantes
    print("\nREPORTE DE ESTUDIANTES")
    print("=" * 40)
    for est in estudiantes:
        print(f"\nNombre: {est['nombre']}")
        print(f"Edad: {est['edad']} años")
        print(f"Grado: {est['grado']}")
        if est["calificaciones"]:
            print("Notas:")
            for cal in est["calificaciones"]:
                print(f"  - {cal['materia']}: {cal['nota']}")
            print(f"Promedio: {calcular_promedio(est['nombre'])}")
        else:
            print("Sin notas registradas")
        print("-" * 30)


print("SISTEMA DE REGISTRO DE ESTUDIANTES")

agregar_estudiante("Luis Torres", 14, "8°")
agregar_estudiante("Sofía Ramírez", 16, "10°")
agregar_estudiante("Julián Pérez", 15, "9°")

registrar_nota("Luis Torres", "Matemáticas", 7.8)
registrar_nota("Luis Torres", "Ciencias", 8.3)
registrar_nota("Sofía Ramírez", "Historia", 9.5)
registrar_nota("Sofía Ramírez", "Lengua", 8.9)
registrar_nota("Julián Pérez", "Matemáticas", 6.7)
registrar_nota("Camila Díaz", "Ciencias", 9.0)

mostrar_reporte()
