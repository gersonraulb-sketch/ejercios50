n1 = float(input("Ingrese su nota: (1.0 , 10.0) "))

if n1 <= 2.0:
    print("Su calificacion es muy baja") # Nota inferior a 2.0
elif 2.0< n1 <= 7.0:
    print("Su calificacion es promedio") # Nota promedio menor a 5.0
elif 7.0 < n1 <= 10.0:
    print("Su calificación es superior") # Nota superior a 7.0
else:
    print("nota invalida")
