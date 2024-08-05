from clase_jugador import Jugador

class JugadorColocador(Jugador):
    def __init__(self):
        """Inicializa un jugador colocador."""
        super().__init__()

    def establecer_combinacion(self):
        """
        Permite al jugador colocador establecer la combinación de colores.
        El jugador debe ingresar una combinación de 4 colores válidos.
        """
        colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosado', 'blanco', 'negro']
        while True:
            combinacion_str = input("Establece la combinación de 4 colores\n"
                                    "(colores permitidos son\n" 
                                    "'rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosado', 'blanco', 'negro')\n"
                                    "(separados por espacio): ")
            self.combinacion = combinacion_str.lower().split()
            if len(self.combinacion) == 4 and all(c in colores for c in self.combinacion):
                break
            else:
                print("Combinación inválida. Asegúrate de ingresar exactamente 4 colores válidos.")
