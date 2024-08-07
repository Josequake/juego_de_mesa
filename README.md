clase jugador
linea 4
Inicializa un jugador con una combinación vacía.
linea 6
Método para establecer la combinación de colores.
Este método debe ser implementado por las subclases.
linea 10
Método para adivinar una combinación de colores.
Este método debe ser implementado por las subclases.

clase jugador_que_adivina
hereda de clase jugador
linea 5
Inicializa el jugador que adivina
linea 9
Permite al jugador que adivina hacer un intento de combinación.
El jugador debe ingresar una combinación de 4 colores válidos.
linea 23
Genera un intento aleatorio de adivinanza para la máquina.
:return: Lista con la combinación de colores adivinada.

clase jugador_que_coloca
hereda de clase jugador
linea 4 
Inicializa el jugador que coloca la combinacion.
linea 8
Permite al jugador que colocador establecer la combinación de colores.
El jugador debe ingresar una combinación de 4 colores válidos.
        
clase tablero
linea 2
Inicializa el tablero con una lista de intentos vacía.
linea 6
Muestra todos los intentos realizados junto con las pistas proporcionadas.
linea 14
Agrega un intento al historial del tablero y muestra el estado actualizado.
:param intento: Lista con los colores adivinados en el intento.
:param pista: La pista proporcionada para el intento.
        
game
se importa ramdon para que la maquina establezca la combinacion de los 4 colores
de igual forma se importa time para que la maquina simule jugar como un usuario y no responda los 12 intentos de un solo tiro
y se importan las clases anteriormente nombradas
linea 8
Inicializa el juego con jugadores, tablero y configuraciones básicas.
linea 15
Inicia el juego preguntando al usuario si quiere ser el colocador o el adivinador.
linea 33
Gestiona el juego cuando el usuario es el adivinador.
Permite al adivinador intentar adivinar la combinación generada por la máquina.
linea 45
Gestiona el juego cuando el usuario es el colocador.
La máquina intenta adivinar la combinación del colocador.
linea 59
Genera una pista comparando el intento con la combinación.
La pista indica cuántos colores están en el lugar correcto (verdes), cuántos están en la combinación pero en la posición incorrecta (naranjas),
y vacíos para los colores que no están en la combinación.
:param intento: Lista de colores en el intento del jugador o máquina.
:param combinacion: Lista de colores en la combinación correcta.
:return: Lista con la pista proporcionada.
linea 84
 Genera una combinación aleatoria de 4 colores para la máquina cuando el usuario es el adivinador.
:return: Lista con la combinación de colores generada.

main
se importa game
linea 3
Función principal que inicia el juego.
se declara una variable que viene siendo el llamado del objeto game 
se declara otra variable donde da inicio al juego y en la funcion principal se llama al mae para que corra sin ningun problema
    

        
             