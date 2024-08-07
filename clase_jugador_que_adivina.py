from clase_jugador import Jugador
import random

class JugadorAdivinador(Jugador):
    def __init__(self):
        
        super().__init__()

    def establecer_adivinanza(self):
       
        colores = ['rojo', 'naranja', 'amarillo', 'verde', 'azul', 'morado', 'cafe', 'negro', 'blanco']
        while True:
            intento_str = input("Adivina la combinación de 4 colores\n"
                                "(colores permitidos son\n" 
                                "'🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '🟤', '⚫', '⚪')\n"
                                "(separados por espacio): ")
            intento = intento_str.lower().split()
            if len(intento) == 4 and all(c in colores for c in intento):
                return intento
            else:
                print("Intento inválido. Asegúrate de ingresar exactamente 4 colores válidos.")
    
    def adivinanza_por_la_maquina(self):
       
        colores = ['rojo', 'naranja', 'amarillo', 'verde', 'azul', 'morado', 'cafe', 'negro', 'blanco']
        return [random.choice(colores) for _ in range(4)]
