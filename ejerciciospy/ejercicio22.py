def sumar(a, b):  # Suma los números
    return a + b


def restar(a, b):  # Resta los números
    return a - b


def multiplicar(a, b):  # Multiplica los números
    return a * b


def dividir(a, b):  # Divide los números
    return a / b if b != 0 else "Error: No se puede dividir entre cero"


# Pedir los números
n1 = float(input("Escribe el primer número: "))
n2 = float(input("Escribe el segundo número: "))

# Mostrar resultados
print("\nCALCULADORA CON FUNCIONES")
print(f"{n1} + {n2} = {sumar(n1, n2)}")
print(f"{n1} - {n2} = {restar(n1, n2)}")
print(f"{n1} * {n2} = {multiplicar(n1, n2)}")
print(f"{n1} / {n2} = {dividir(n1, n2)}")
