class Jugador:
    def __init__(self):
        
        self.combinacion = []

    def establecer_combinacion(self):
        
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def establecer_adivinanza(self):
       
        raise NotImplementedError("Este método debe ser implementado en las subclases")
