total = int(input("Ingrese el total de su factura: "))
descuento = 0.15

if total >= 300:
    des = total * descuento # descuento del 15%
    des_total = total - des # aplicar el descuento
    print(f"Tiene un descuento del 15%, su factura queda en {des_total}") # Descuento valido
else:
    total > 300
    print(f"No tiene descuentos disponible") # Descuento invalido

