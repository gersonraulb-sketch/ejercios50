import random


class Animal:
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.tipo = tipo  # "herbívoro" o "carnívoro"
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        """Mueve el animal aleatoriamente"""
        if self.vivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5
            if self.energia <= 0:
                self.vivo = False
                print(f"{self.nombre} ha muerto de cansancio/energía baja.")

    def comer(self, otro):
        """Depredadores cazan, herbívoros recuperan energía si 'comen hierba'"""
        if not self.vivo:
            return
        if self.tipo == "carnívoro" and otro.vivo and otro.tipo == "herbívoro":
            self.energia += 40
            otro.vivo = False
            print(
                f"{self.nombre} se comió a {otro.nombre}. Energía ahora: {self.energia}")
        elif self.tipo == "herbívoro":
            # El herbívoro recupera energía como si encontrara hierba
            self.energia += 20
            print(f"{self.nombre} comió hierba. Energía ahora: {self.energia}")

    def estado(self):
        return f"{self.nombre} ({self.tipo}) - Energía: {self.energia}, Pos: ({self.posicion_x}, {self.posicion_y}), Vivo: {self.vivo}"


# Simulación
animales = [
    Animal("Conejo1", "herbívoro"),
    Animal("Conejo2", "herbívoro"),
    Animal("Lobo1", "carnívoro")
]

print("INICIO DEL ECOSISTEMA")
print("=" * 40)

for turno in range(1, 6):
    print(f"\n--- Turno {turno} ---")
    for animal in animales:
        animal.mover()
        # Los carnívoros intentan comer si hay herbívoros cerca
        if animal.tipo == "carnívoro":
            for presa in animales:
                if presa.tipo == "herbívoro" and presa.vivo:
                    if abs(animal.posicion_x - presa.posicion_x) <= 1 and abs(animal.posicion_y - presa.posicion_y) <= 1:
                        animal.comer(presa)
        # Los herbívoros comen hierba con cierta probabilidad
        if animal.tipo == "herbívoro" and random.random() < 0.5:
            animal.comer(None)

    # Mostrar estado de todos los animales
    for animal in animales:
        print(animal.estado())
