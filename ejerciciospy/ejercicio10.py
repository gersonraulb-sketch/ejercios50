# Pide al usuario que cree una contraseña
contraseña = input("Cree una contraseña (min 10 caracteres): ")

if len(contraseña) < 10: # Si la contraseña tiene menos de 10 caracteres
    print("Su contraseña no cumple el minimo de caracteres")

elif contraseña.isdigit(): # Si la contraseña solo contiene números
    print("La contraseña no puede contener solo números")

else: # Si cumple con ambas condiciones
    print("Su contraseña se ha creado con éxito")