from clase_jugador import Jugador

class JugadorColocador(Jugador):
    def __init__(self):
        
        super().__init__()

    def establecer_combinacion(self):
      
        colores = ['rojo', 'naranja', 'amarillo', 'verde', 'azul', 'morado', 'cafe', 'negro', 'blanco']
        while True:
            combinacion_str = input("Establece la combinación de 4 colores\n"
                                    "(colores permitidos son\n" 
                                    "'🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '🟤', '⚫', '⚪')\n"
                                    "(separados por espacio): ")
            self.combinacion = combinacion_str.lower().split()
            if len(self.combinacion) == 4 and all(c in colores for c in self.combinacion):
                break
            else:
                print("Combinación inválida. Asegúrate de ingresar exactamente 4 colores válidos.")
