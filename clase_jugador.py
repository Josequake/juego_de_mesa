class Jugador:
    def __init__(self):
        """Inicializa un jugador con una combinación vacía."""
        self.combinacion = []

    def establecer_combinacion(self):
        """
        Método para establecer la combinación de colores.
        Este método debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def establecer_adivinanza(self):
        """
        Método para adivinar una combinación de colores.
        Este método debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado en las subclases")
