class Tablero:
    def __init__(self):
        """Inicializa el tablero con una lista de intentos vacía."""
        self.intentos = []

    def mostrar_intentos(self):
        """
        Muestra todos los intentos realizados junto con las pistas proporcionadas.
        """
        if not self.intentos:
            print("No se han realizado intentos aún.")
        else:
            for num, (intento, pista) in enumerate(self.intentos, start=1):
                print(f"Intento {num}: {intento} -> {pista}")

    def agregar_intento(self, intento, pista):
        """
        Agrega un intento al historial del tablero y muestra el estado actualizado.
        
        :param intento: Lista con los colores adivinados en el intento.
        :param pista: La pista proporcionada para el intento.
        """
        self.intentos.append((intento, pista))
        self.mostrar_intentos()
        print()
