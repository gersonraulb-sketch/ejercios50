n1 = int(input("Ingrese su numero en un rango de 1 a 20: "))
num_secreto = 15 # Numero secreto

if n1 < num_secreto: # Si el numero es mayor al secreto
    print("El numero secreto es mayor, intentalo de nuevo") 
elif n1 > num_secreto: # Si el numero es menor al secreto
    print("El numero secreto es menor, intentalo de nuevo")
elif n1 == num_secreto: # Si el numero es igual al secreto
    print("Felicidades haz descubierto el numero secreto")
