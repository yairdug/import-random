import random

class Casa:
    def __init__(self, nombre, lema):
        self.nombre = nombre
        self.lema = lema

    def __str__(self):
        return f"Casa {self.nombre} — '{self.lema}'"


class Personaje:
    def __init__(self, nombre, casa, poder):
        self.nombre = nombre
        self.casa = casa
        self.poder = poder  # valor de 1 a 100

    def presentar(self):
        print(f"{self.nombre} de la {self.casa.nombre} (Poder: {self.poder})")

    def combatir(self, enemigo):
        print(f"\n⚔️  {self.nombre} lucha contra {enemigo.nombre}...")
        resultado = self.poder + random.randint(-10, 10) - (enemigo.poder + random.randint(-10, 10))

        if resultado > 0:
            print(f"🏆 {self.nombre} ha ganado el combate.")
        elif resultado < 0:
            print(f"💀 {enemigo.nombre} ha ganado el combate.")
        else:
            print("🤝 El combate termina en empate.")


# Crear casas
stark = Casa("Stark", "El invierno se acerca")
lannister = Casa("Lannister", "Oye mi rugido")

# Crear personajes
jon = Personaje("Jon Snow", stark, poder=85)
jaime = Personaje("Jaime Lannister", lannister, poder=80)

# Presentación
print("=== Personajes ===")
jon.presentar()
jaime.presentar()

# Combate
jon.combatir(jaime)
