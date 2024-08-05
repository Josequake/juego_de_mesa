from clase_jugador import Jugador
import random

class JugadorAdivinador(Jugador):
    def __init__(self):
        """Inicializa un jugador adivinador."""
        super().__init__()

    def establecer_adivinanza(self):
        """
        Permite al jugador adivinador hacer un intento de combinación.
        El jugador debe ingresar una combinación de 4 colores válidos.
        """
        colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosado', 'blanco', 'negro']
        while True:
            intento_str = input("Adivina la combinación de 4 colores\n"
                                "(colores permitidos son\n" 
                                "'rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosado', 'blanco', 'negro')\n"
                                "(separados por espacio): ")
            intento = intento_str.lower().split()
            if len(intento) == 4 and all(c in colores for c in intento):
                return intento
            else:
                print("Intento inválido. Asegúrate de ingresar exactamente 4 colores válidos.")
    
    def adivinanza_por_la_maquina(self):
        """
        Genera un intento aleatorio de adivinanza para la máquina.

        :return: Lista con la combinación de colores adivinada.
        """
        colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosado', 'blanco', 'negro']
        return [random.choice(colores) for _ in range(4)]
