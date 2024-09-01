import random

def jugar_ruleta():
    print("¡Bienvenido al juego de Ruleta!")
    print("Apuesta en un número entre 0 y 36.")
    
    # Obtener la apuesta del jugador
    try:
        apuesta = int(input("Introduce tu apuesta (número entre 0 y 36): "))
        if apuesta < 0 or apuesta > 36:
            print("Número inválido. Debe estar entre 0 y 36.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")
        return
    
    # Generar el resultado de la ruleta
    resultado = random.randint(0, 36)
    print(f"La ruleta ha salido en: {resultado}")

    # Determinar si el jugador ha ganado
    if apuesta == resultado:
        print("¡Felicidades! Has ganado.")
    else:
        print("Lo siento, has perdido. Intenta de nuevo.")

if __name__ == "__main__":
    jugar_ruleta()
