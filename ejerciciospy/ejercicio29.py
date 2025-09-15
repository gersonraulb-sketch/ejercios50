def es_primo_simple(n):  # Verifica si un número es primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def criba_eratostenes(limite):  # Genera una lista de números primos hasta un límite
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False

    return [i for i, primo in enumerate(es_primo) if primo]


def factorizacion_prima(n):
    """Devuelve los factores primos de un número"""
    factores = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factores.append(n)
    return factores


# Pruebas
print("1. Verificación de primos:")
for num in [17, 25, 29]:
    print(f"{num} es primo? {es_primo_simple(num)}")

print("\n2. Criba de Eratóstenes hasta 30:")
primos = criba_eratostenes(30)
print("Primos encontrados:", primos)

print("\n3. Factorización prima de 60:")
factores = factorizacion_prima(60)
print("60 =", " × ".join(map(str, factores)))
