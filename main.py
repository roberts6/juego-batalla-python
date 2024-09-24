# -------------------------------------------

# Juego

# -------------------------------------------
from jugador import Jugador
from enemigo import Enemigo
import random
import sys  

def main():
    nombre_jugador = input("¡Bienvenido! ¿Cómo es tu nombre? ")
    jugador = Jugador(nombre_jugador)  # Instancia de la clase Jugador
    
    # Enemigos con experiencia que otorgan al ser derrotados
    enemigos = [
        Enemigo("Alien", 50, 10, 50),       # El último número representa la experiencia otorgada
        Enemigo("Robot", 60, 12, 60),
        Enemigo("Dinosaurio", 70, 18, 80)
    ]
    
    print("¡Comienza la BATALLA...!")

    while True:
        enemigo_actual = random.choice(enemigos)
        print(f"¡Cuidado! Tu enemigo ahora es {enemigo_actual.nombre}.")

        # Ciclo de combate con el enemigo actual
        while enemigo_actual.salud > 0 and jugador.salud > 0:
            accion = input(f"{nombre_jugador}, ¿qué deseas hacer? (atacar / huir / salir)? ").lower()

            if accion == "atacar":
                # Jugador ataca
                dano_jugador = jugador.atacar()  
                enemigo_actual.salud -= dano_jugador
                if enemigo_actual.salud <= 0:
                    print(f"¡Has derrotado a {enemigo_actual.nombre}!")
        
                    # Ganar experiencia por derrotar al enemigo
                    jugador.ganar_experiencia(enemigo_actual.experiencia)
                    if jugador.experiencia <= 100:
                        print(f"Subiste tu nivel de experiencia a {jugador.experiencia}!")
                    else:
                        print(f"Subiste a un nuevo nivel {jugador.nivel}!")
                    break  # Terminar el ciclo de combate y elegir uno nuevo
                else:
                    print(f"Has atacado a {enemigo_actual.nombre} y le causaste un daño de {dano_jugador}. Su salud ahora es {enemigo_actual.salud}.")

                # Enemigo ataca si aún está vivo
                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    jugador.recibir_dano(dano_enemigo)  
                    if jugador.salud <= 0:
                        print(f"{enemigo_actual.nombre} te ha atacado y te ha causado un daño mortal 💀")
                        print("¡Has sido derrotado! ¡Juego terminado!")
                        print("💀💀💀💀💀💀💀💀💀")
                        sys.exit()  # Terminar el juego si el jugador es derrotado

            elif accion == "huir":
                print(f"Has huido de {enemigo_actual.nombre}.")
                break
            elif accion == "salir":
                print(f"Gracias por jugar {nombre_jugador}. ¡Hasta la próxima!")
                sys.exit()  # Cierra el programa
            else:
                print("Acción no válida. Por favor elige 'atacar', 'huir' o 'salir'.")

if __name__ == "__main__": # asegura que solo se pueda ejecutar el script desde el programa principal.
# Ejecutar el juego
    main()