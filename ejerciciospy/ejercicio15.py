n1 = int(input("Ingrese su numero en un rango de 1 a 20: "))  # Pide un número inicial al usuario (aunque no se usa luego)

num_secreto = 46  # Número secreto a adivinar (estático)
intentos = 0      # Contador de intentos realizados
max_inte = 3      # Número máximo de intentos permitidos

while intentos < max_inte:  # Se repite mientras no se excedan los intentos máximos
    intento = input("Ingrese su numero: ")  # Pide un nuevo intento al usuario
    intentos += 1  # Aumenta el contador de intentos

    if intento < num_secreto:  # Compara si el intento es menor que el número secreto
        print("Muy bajo")
    elif intento > num_secreto:  # Compara si el intento es mayor que el número secreto
        print("Muy alto")
    else:
        print("¡Ganaste!")  # El número es correcto
        break  # Sale del bucle si se adivina correctamente

else:
    print("Haz alcanzado el maximo de intentos")  # Se ejecuta si se agotan todos los intentos sin adivinar
