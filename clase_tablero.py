class Tablero:
    def __init__(self):
        
        self.intentos = []

    def mostrar_intentos(self):
        
        if not self.intentos:
            print("No se han realizado intentos aún.")
        else:
            for num, (intento, pista) in enumerate(self.intentos, start=1):
                print(f"Intento {num}: {intento} -> {pista}")

    def agregar_intento(self, intento, pista):
       
        self.intentos.append((intento, pista))
        self.mostrar_intentos()
        print()
