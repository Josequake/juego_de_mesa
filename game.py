import random
import time
from clase_jugadorColocador import JugadorColocador
from clase_jugadorAdivinador import JugadorAdivinador
from clase_tablero import Tablero

class Game:
    def __init__(self):
        """Inicializa el juego con jugadores, tablero y configuraciones básicas."""
        self.jugador_colocador = None
        self.jugador_adivinador = None
        self.tablero = Tablero()
        self.max_intentos = 12  # Número máximo de intentos permitidos

    def iniciar(self):
        """
        Inicia el juego preguntando al usuario si quiere ser el colocador o el adivinador.
        """
        print("Bienvenido al juego de mesa Mastermind")
        eleccion = input("¿Desea ser el jugador colocador? presione (1) o el jugador adivinador? presione (2)? ").lower()
        if eleccion == '1':
            self.jugador_colocador = JugadorColocador()
            self.jugador_colocador.establecer_combinacion()
            self.jugador_adivinador = JugadorAdivinador()
            self.jugar_colocador()
        elif eleccion == '2':
            self.jugador_adivinador = JugadorAdivinador()
            self.jugar_adivinador()
        else:
            print("Opción inválida. Intenta de nuevo.")
            self.iniciar()

    def jugar_adivinador(self):
        """
        Gestiona el juego cuando el usuario es el adivinador.
        Permite al adivinador intentar adivinar la combinación generada por la máquina.
        """
        combinacion = self.generar_combinacion()
        for intento_num in range(self.max_intentos):
            intento = self.jugador_adivinador.establecer_adivinanza()
            pista = self.obtener_pista(intento, combinacion)
            self.tablero.agregar_intento(intento, pista)
            if pista == ['verde', 'verde', 'verde', 'verde']:
                print(f"¡Ganaste! Adivinaste la combinación en {intento_num + 1} intentos.")
                return
        print(f"Perdiste. La combinación correcta era {combinacion}.")

    def jugar_colocador(self):
        """
        Gestiona el juego cuando el usuario es el colocador.
        La máquina intenta adivinar la combinación del colocador.
        """
        combinacion = self.jugador_colocador.combinacion
        self.jugador_adivinador = JugadorAdivinador()  # Inicializa al adivinador para usar su método de adivinanza
        for intento_num in range(self.max_intentos):
            intento = self.jugador_adivinador.adivinanza_por_la_maquina()
            pista = self.obtener_pista(intento, combinacion)
            self.tablero.agregar_intento(intento, pista)
            if pista == ['verde', 'verde', 'verde', 'verde']:
                print(f"La máquina adivinó tu combinación en {intento_num + 1} intentos.")
                return
            time.sleep(2)  # Simula el tiempo que toma la máquina en adivinar
        print(f"La máquina no logró adivinar la combinación. La combinación era {combinacion}.")

    def obtener_pista(self, intento, combinacion):
        """
        Genera una pista comparando el intento con la combinación.
        La pista indica cuántos colores están en el lugar correcto (verdes), cuántos están en la combinación pero en la posición incorrecta (naranjas),
        y vacíos para los colores que no están en la combinación.

        :param intento: Lista de colores en el intento del jugador o máquina.
        :param combinacion: Lista de colores en la combinación correcta.
        :return: Lista con la pista proporcionada.
        """
        pista = [''] * len(intento)  # Inicializa la pista con cadenas vacías
        combinacion_usada = [False] * len(combinacion)
        intento_usado = [False] * len(intento)
        
        # Primer paso: Identificar los colores correctos y en la posición correcta (verdes)
        for i in range(len(intento)):
            if intento[i] == combinacion[i]:
                pista[i] = 'verde'
                combinacion_usada[i] = True
                intento_usado[i] = True
        
        # Segundo paso: Identificar los colores correctos pero en la posición incorrecta (naranjas)
        for i in range(len(intento)):
            if not intento_usado[i]:
                for j in range(len(combinacion)):
                    if not combinacion_usada[j] and intento[i] == combinacion[j]:
                        if pista[i] != 'verde':  # Solo agregar 'naranja' si no es 'verde'
                            pista[i] = 'naranja'
                        combinacion_usada[j] = True
                        break
        
        return pista

    def generar_combinacion(self):
        """
        Genera una combinación aleatoria de 4 colores para la máquina cuando el usuario es el adivinador.

        :return: Lista con la combinación de colores generada.
        """
        colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado']
        return [random.choice(colores) for _ in range(4)]
