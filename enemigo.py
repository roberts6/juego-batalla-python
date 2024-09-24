import random


class Enemigo:
    def __init__(self, nombre, salud, dano, experiencia):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano
        self.experiencia = experiencia
        
    def atacar(self):
        return random.randint(10 , 20)
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            print(f"Has derrotado a {self.nombre}")
            return True
        return False