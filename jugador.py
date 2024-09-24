import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100 # valor harckodeado
        self.nivel = 1 # valor harckodeado
        self.experiencia = 0 # valor harckodeado
        
    def atacar(self):
        return random.randint(10, 20) * self.nivel
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            print("💀💀💀💀💀💀💀💀💀")
        else:
            print(f"tu nivel de vida actual es {self.salud}")
            
    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} alcanzaste el nivel más alto de experiencia {self.experiencia} y subiste al nivel {self.nivel}")